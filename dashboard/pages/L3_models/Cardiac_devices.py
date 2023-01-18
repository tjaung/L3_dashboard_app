
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Cardiac_devices_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Cardiac_devices"
    joblib_file = model_dir + "/Cardiac_devices.joblib"
    dill_file = model_dir + "/Cardiac_devices.dill"
    yaml_file = model_dir + "/Cardiac_devices_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Cardiac devices']['author']

db = ExplainerDashboard(get_Cardiac_devices_dashboard(), 
    title='Cardiac devices', 
    name='Cardiac_devices')
   # description="Created by: " + author)

