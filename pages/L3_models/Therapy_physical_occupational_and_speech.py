
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

def get_Therapy_physical_occupational_and_speech_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Therapy_physical_occupational_and_speech")
    #joblib_file = model_dir + "/Therapy_physical_occupational_and_speech.joblib"
    dill_file = model_dir + "/Therapy_physical_occupational_and_speech.dill"
    #yaml_file = model_dir + "/Therapy_physical_occupational_and_speech_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    # convert dtypes to versions for memory improvement
    ints = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    floats = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    clas_explainer.X = clas_explainer.X.astype(ints)
    clas_explainer.X = clas_explainer.X.astype(floats)
    
    print(clas_explainer.memory_usage())

    return clas_explainer

#author = MODELS_BY_PAL['Therapy physical occupational and speech']['author']

db = ExplainerDashboard(get_Therapy_physical_occupational_and_speech_dashboard(), 
    title='Therapy physical occupational and speech', 
    name='Therapy_physical_occupational_and_speech',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA,
    whatif=False,
    importances=False,
    shap_interaction=False)

