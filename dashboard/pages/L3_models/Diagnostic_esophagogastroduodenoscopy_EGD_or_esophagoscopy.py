
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy"
    joblib_file = model_dir + "/Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy.joblib"
    dill_file = model_dir + "/Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy.dill"
    yaml_file = model_dir + "/Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Diagnostic esophagogastroduodenoscopy EGD or esophagoscopy']['author']

db = ExplainerDashboard(get_Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy_dashboard(), 
    title='Diagnostic esophagogastroduodenoscopy EGD or esophagoscopy', 
    name='Diagnostic_esophagogastroduodenoscopy_EGD_or_esophagoscopy')
   # description="Created by: " + author)

