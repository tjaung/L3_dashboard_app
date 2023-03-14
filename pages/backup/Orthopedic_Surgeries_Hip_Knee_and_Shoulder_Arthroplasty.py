
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

def get_Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty")
    #joblib_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty.joblib"
    dill_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty.dill"
    #yaml_file = model_dir + "/Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    # convert dtypes to versions for memory improvement
    # ints = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # floats = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # clas_explainer.X = clas_explainer.X.astype(ints)
    # clas_explainer.X = clas_explainer.X.astype(floats)
    
    print(clas_explainer.memory_usage())

    return clas_explainer

#author = MODELS_BY_PAL['Orthopedic Surgeries Hip Knee and Shoulder Arthroplasty']['author']

db = ExplainerDashboard(get_Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty_dashboard(), 
    title='Orthopedic Surgeries Hip Knee and Shoulder Arthroplasty', 
    name='Orthopedic_Surgeries_Hip_Knee_and_Shoulder_Arthroplasty',
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA,
    whatif=False,
    importances=False,
    shap_interaction=False)

