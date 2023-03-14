from pathlib import Path
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import explainerdashboard
from explainerdashboard import ClassifierExplainer, ExplainerHub, ExplainerDashboard
from backend.data_pull import MODELS_BY_PAL
import backend.get_shap as gs
import pickle
import pandas as pd
import numpy as np
import os
import dill
import dash
from flask import Flask
import backend.s3_pull as s3_pull
from pprint import pprint
import importlib
from datetime import date
import dash_bootstrap_components as dbc
import warnings
import shap


warnings.simplefilter(action='ignore', category=FutureWarning)
#warnings.simplefilter(action='ignore', category=SettingWithCopyWarning)

app = Flask(__name__)


def create_directory_if_not_exist(path):
    # make dir if not exist
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

def dump_explainer_files(explainer, model, path):

    explainer.dump(path / f"{model}.dill")
  #  explainer.to_joblib(path / f"{model}.joblib")
    explainer.to_yaml(path / f"{model}_dashboard.yaml")

def generate_python_code_for_dashboard(dir, model_name, service):
    model_title = model_name.replace('_', ' ')
    model_name = model_name.replace(' ', '_').replace(':', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '')
    
    return f'''
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

def get_{model_name}_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/{model_name}")
    #joblib_file = model_dir + "/{model_name}.joblib"
    dill_file = model_dir + "/{model_name}.dill"
    #yaml_file = model_dir + "/{model_name}_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    # convert dtypes to versions for memory improvement
    # ints = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # floats = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # clas_explainer.X = clas_explainer.X.astype(ints)
    # clas_explainer.X = clas_explainer.X.astype(floats)
    
    print(clas_explainer.memory_usage())

    return clas_explainer

#author = MODELS_BY_PAL['{model_title}']['author']

db = ExplainerDashboard(get_{model_name}_dashboard(), 
    title='{model_title}', 
    name='{model_name}',
    description="{service.upper().replace('_', ' ')} L3 Model",
    bootstrap=dbc.themes.LITERA,
    whatif=False,
    importances=False,
    shap_interaction=False)

'''

#@app.route('/dashboard/')
def generate_dashboard(data, model, params):
    
    model_name = params['pal'].replace(' ', '_').replace(':', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '')
    dir = Path.cwd() / 'modelFiles'
   # dir = os.path.abspath(os.curdir)

    #initialize explainer
    n = 1000 if len(data['X_test']) > 1000 else len(data['X_test'])

    explainer = ClassifierExplainer(model, 
                                    data['X_test'], 
                                    data['y_test'], 
                                    X_background=shap.sample(data['X_test'], 30),
                                    model_output='probability',
                                shap='kernel',
                                precision='float16',
                                labels=['Approve', 'Pend'])
    ints = dict.fromkeys(explainer.X.select_dtypes(np.int64).columns, np.int8)
    floats = dict.fromkeys(explainer.X.select_dtypes(np.int64).columns, np.int8)
    explainer.X = explainer.X.astype(ints)
    explainer.X = explainer.X.astype(floats)

    # pre generate shap and load
    #shap_params = gs.create_shap_vals(data['X_test'], model)
    #explainer.set_shap_values(shap_params[0], shap_params[1])

    _ = ExplainerDashboard(explainer)

  #  generate_dash_files(dir, model_name, explainer, params)

    return {'dir': dir,
            'model_name': model_name,
            'explainer': explainer}



def generate_dash_files(dir, model_name, explainer, params):
    fname = 'dir'
    print(f'Writing {model_name} Dashboard File: {fname}', end='\r')
    # make dir if not exist
    create_directory_if_not_exist(dir / f"{model_name}")
    
    # dump files
    fname = 'dill'
    print(f'Writing {model_name} Dashboard File: {fname}', end='\r')
    dump_explainer_files(explainer, model_name, dir/f"{model_name}")

    # generate code for dashboard file
    fname = 'script'
    print(f'Writing {model_name} Dashboard File: {fname}', end='\r')
    code = generate_python_code_for_dashboard(dir, model_name, params['service'])

    # write code
    with open( Path.cwd()/f'pages/L3_models/{model_name}.py', 'w' ) as fout :
        fout.write( code )
    
    
    print(f'Writing {model_name} Dashboard Files: Done!', end='\r')


def get_dash_info(service, p):
    params = s3_pull.get_model_params_from_s3_buckets(service, p)
    #pprint(params)

    # pull model
    model = s3_pull.get_model(params)

    # pull data
    data = s3_pull.load_cleaned_train_test(params, model)

    return {'params': params, 
            'model': model, 
            'data': data}

def generate_pages():
    fail = False
    dashes = []
    service_types = ['msk', 'cardio', 'surgical_services']
    for service in service_types:
        fail = False
        # get pal directory:
        pals = []

        for dir in s3_pull.list_s3_subdirectories(f'signal_based_models/{service}/by_PAL/'):
            
            p = os.path.basename(os.path.normpath(dir))
            pals.append(p)
            print(p)
            pal_file = p.replace(' ', '_').replace(':', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '')

            #check for already existiing dash
            if not os.path.exists(Path.cwd()/f'pages/L3_models/{pal_file}.py'):
                info = get_dash_info(service, p)

                try:
                    # make dashboard
                    if len(info['data']['X_test']) != len(info['data']['y_test']):
                        print('Size of data X and y not the same. Skipping dashboard generation...')
                        continue
                    
                    dash_info = generate_dashboard(info['data'], info['model'], info['params'])
                    generate_dash_files(dash_info['dir'], dash_info['model_name'], dash_info['explainer'], info['params'])
                except:
                    fail = True
                    pass
            if fail:
                pass
            else:
                # add to hub
                module = 'pages.L3_models.' + pal_file
                print('================================================')
                print(module)
                Y = getattr(importlib.import_module(module), 'db')
                print(Y)
                dashes.append(Y)
                print("================================================")
            
            
    # save the hub dashboard yaml
    #hub.add_user('cohere_user', 'show_m3_the_$')
    #today = date.today()
    #hub_v = f'modelFiles/humana_dashboards_{today}.yaml'
    #hub.to_yaml(Path.cwd()/hub_v)
    
    hub = ExplainerHub(dashes, title="Data Science Team L3 Models",
            description="Dashboards for the Humana L3 Models created by the DS team.",
           # no_index=True)#,
            add_dashboard_route=True,
            bootstrap=dbc.themes.LITERA)
#            index_to_base_route=True)
    
    return hub

def generate_from_py_scripts(exclude=[]):
    dashes = []
    for page in os.listdir(Path.cwd()/'pages/L3_models/'):
        if page in exclude or page == exclude:
            print(f'Excluding dashboard: {page}')
            continue
        page = 'pages.L3_models.' + page
        print(page)
        Y = getattr(importlib.import_module(page), 'db')
        #print(Y)
        dashes.append(Y)

    hub = ExplainerHub(dashes, title="Data Science Team L3 Models",
            description="Dashboards for the Humana L3 Models created by the DS team.",
           # no_index=True)#,
            add_dashboard_route=True,
            bootstrap=dbc.themes.LITERA)
#            index_to_base_route=True)
    
    return hub