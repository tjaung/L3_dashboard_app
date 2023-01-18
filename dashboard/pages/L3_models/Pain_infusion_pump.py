
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Pain_infusion_pump_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Pain_infusion_pump"
    joblib_file = model_dir + "/Pain_infusion_pump.joblib"
    dill_file = model_dir + "/Pain_infusion_pump.dill"
    yaml_file = model_dir + "/Pain_infusion_pump_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Pain infusion pump']['author']

db = ExplainerDashboard(get_Pain_infusion_pump_dashboard(), 
    title='Pain infusion pump', 
    name='Pain_infusion_pump')
   # description="Created by: " + author)

