
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty"
    joblib_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty.joblib"
    dill_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty.dill"
    yaml_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Orthopedic Surgeries Hip, Knee and Shoulder Arthroplasty']['author']

db = ExplainerDashboard(get_Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard(), 
    title='Orthopedic Surgeries Hip, Knee and Shoulder Arthroplasty', 
    name='Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty')
   # description="Created by: " + author)

