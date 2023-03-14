
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

def get_Facet_injections_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Facet_injections")
    #joblib_file = model_dir + "/Facet_injections.joblib"
    dill_file = model_dir + "/Facet_injections.dill"
    #yaml_file = model_dir + "/Facet_injections_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    # convert dtypes to versions for memory improvement
    # ints = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # floats = dict.fromkeys(clas_explainer.X.select_dtypes(np.int64).columns, np.int8)
    # clas_explainer.X = clas_explainer.X.astype(ints)
    # clas_explainer.X = clas_explainer.X.astype(floats)
    
    print(clas_explainer.memory_usage())

    return clas_explainer

#author = MODELS_BY_PAL['Facet injections']['author']

db = ExplainerDashboard(get_Facet_injections_dashboard(), 
    title='Facet injections', 
    name='Facet_injections',
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA,
    whatif=False,
    importances=False,
    shap_interaction=False)

