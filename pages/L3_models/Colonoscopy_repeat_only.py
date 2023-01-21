
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Colonoscopy_repeat_only_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Colonoscopy_repeat_only")
    #joblib_file = model_dir + "/Colonoscopy_repeat_only.joblib"
    dill_file = model_dir + "/Colonoscopy_repeat_only.dill"
    #yaml_file = model_dir + "/Colonoscopy_repeat_only_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Colonoscopy repeat only']['author']

db = ExplainerDashboard(get_Colonoscopy_repeat_only_dashboard(), 
    title='Colonoscopy repeat only', 
    name='Colonoscopy_repeat_only',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="SURGICAL_SERVICES L3 Model",
    bootstrap=dbc.themes.LITERA)

