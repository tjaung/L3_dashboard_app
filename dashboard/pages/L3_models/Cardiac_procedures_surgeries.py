
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from backend.data_pull import MODELS_BY_PAL

def get_Cardiac_procedures_surgeries_dashboard():
    model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Cardiac_procedures_surgeries"
    joblib_file = model_dir + "/Cardiac_procedures_surgeries.joblib"
    dill_file = model_dir + "/Cardiac_procedures_surgeries.dill"
    yaml_file = model_dir + "/Cardiac_procedures_surgeries_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Cardiac procedures surgeries']['author']

db = ExplainerDashboard(get_Cardiac_procedures_surgeries_dashboard(), 
    title='Cardiac procedures surgeries', 
    name='Cardiac_procedures_surgeries')
   # description="Created by: " + author)

