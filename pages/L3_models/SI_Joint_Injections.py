
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_SI_Joint_Injections_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/SI_Joint_Injections")
    #joblib_file = model_dir + "/SI_Joint_Injections.joblib"
    dill_file = model_dir + "/SI_Joint_Injections.dill"
    #yaml_file = model_dir + "/SI_Joint_Injections_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['SI Joint Injections']['author']

db = ExplainerDashboard(get_SI_Joint_Injections_dashboard(), 
    title='SI Joint Injections', 
    name='SI_Joint_Injections',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA)

