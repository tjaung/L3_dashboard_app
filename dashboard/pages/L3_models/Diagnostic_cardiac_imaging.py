
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Diagnostic_cardiac_imaging_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Diagnostic_cardiac_imaging"
    joblib_file = model_dir + "/Diagnostic_cardiac_imaging.joblib"
    dill_file = model_dir + "/Diagnostic_cardiac_imaging.dill"
    yaml_file = model_dir + "/Diagnostic_cardiac_imaging_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Diagnostic cardiac imaging']['author']

db = ExplainerDashboard(get_Diagnostic_cardiac_imaging_dashboard(), 
    title='Diagnostic cardiac imaging', 
    name='Diagnostic_cardiac_imaging')
   # description="Created by: " + author)

