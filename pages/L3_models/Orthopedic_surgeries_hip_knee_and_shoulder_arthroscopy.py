
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy"
    joblib_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy.joblib"
    dill_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy.dill"
    yaml_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Orthopedic surgeries hip knee and shoulder arthroscopy']['author']

db = ExplainerDashboard(get_Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard(), 
    title='Orthopedic surgeries hip knee and shoulder arthroscopy', 
    name='Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy')
   # description="Created by: " + author)

