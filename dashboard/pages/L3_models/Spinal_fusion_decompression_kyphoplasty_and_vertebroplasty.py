
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty"
    joblib_file = model_dir + "/Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty.joblib"
    dill_file = model_dir + "/Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty.dill"
    yaml_file = model_dir + "/Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Spinal fusion decompression kyphoplasty and vertebroplasty']['author']

db = ExplainerDashboard(get_Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty_dashboard(), 
    title='Spinal fusion decompression kyphoplasty and vertebroplasty', 
    name='Spinal_fusion_decompression_kyphoplasty_and_vertebroplasty')
   # description="Created by: " + author)

