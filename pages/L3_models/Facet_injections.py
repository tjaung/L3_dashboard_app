
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Facet_injections_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Facet_injections")
    #joblib_file = model_dir + "/Facet_injections.joblib"
    dill_file = model_dir + "/Facet_injections.dill"
    #yaml_file = model_dir + "/Facet_injections_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Facet injections']['author']

db = ExplainerDashboard(get_Facet_injections_dashboard(), 
    title='Facet injections', 
    name='Facet_injections',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA)

