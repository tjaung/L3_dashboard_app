
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Spinal_cord_stimulators_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Spinal_cord_stimulators")
    #joblib_file = model_dir + "/Spinal_cord_stimulators.joblib"
    dill_file = model_dir + "/Spinal_cord_stimulators.dill"
    #yaml_file = model_dir + "/Spinal_cord_stimulators_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Spinal cord stimulators']['author']

db = ExplainerDashboard(get_Spinal_cord_stimulators_dashboard(), 
    title='Spinal cord stimulators', 
    name='Spinal_cord_stimulators',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA)

