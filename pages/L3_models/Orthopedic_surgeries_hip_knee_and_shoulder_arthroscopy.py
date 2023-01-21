
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy")
    #joblib_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy.joblib"
    dill_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy.dill"
    #yaml_file = model_dir + "/Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Orthopedic surgeries hip knee and shoulder arthroscopy']['author']

db = ExplainerDashboard(get_Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_dashboard(), 
    title='Orthopedic surgeries hip knee and shoulder arthroscopy', 
    name='Orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA)

