
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

def get_Colonoscopy_repeat_only_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Colonoscopy_repeat_only")
    #joblib_file = model_dir + "/Colonoscopy_repeat_only.joblib"
    dill_file = model_dir + "/Colonoscopy_repeat_only.dill"
    #yaml_file = model_dir + "/Colonoscopy_repeat_only_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    # convert dtypes to versions for memory improvement
    ints = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    floats = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    clas_explainer.X = clas_explainer.X.astype(ints)
    clas_explainer.X = clas_explainer.X.astype(floats)
    
    print(clas_explainer.memory_usage())

    return clas_explainer

#author = MODELS_BY_PAL['Colonoscopy repeat only']['author']

db = ExplainerDashboard(get_Colonoscopy_repeat_only_dashboard(), 
    title='Colonoscopy repeat only', 
    name='Colonoscopy_repeat_only',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="SURGICAL SERVICES L3 Model",
    bootstrap=dbc.themes.LITERA,
    whatif=False,
    importances=False,
    shap_interaction=False)

