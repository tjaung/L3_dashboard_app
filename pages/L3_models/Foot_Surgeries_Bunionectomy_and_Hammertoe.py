
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Foot_Surgeries_Bunionectomy_and_Hammertoe_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Foot_Surgeries_Bunionectomy_and_Hammertoe")
    #joblib_file = model_dir + "/Foot_Surgeries_Bunionectomy_and_Hammertoe.joblib"
    dill_file = model_dir + "/Foot_Surgeries_Bunionectomy_and_Hammertoe.dill"
    #yaml_file = model_dir + "/Foot_Surgeries_Bunionectomy_and_Hammertoe_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Foot Surgeries Bunionectomy and Hammertoe']['author']

db = ExplainerDashboard(get_Foot_Surgeries_Bunionectomy_and_Hammertoe_dashboard(), 
    title='Foot Surgeries Bunionectomy and Hammertoe', 
    name='Foot_Surgeries_Bunionectomy_and_Hammertoe',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="MSK L3 Model",
    bootstrap=dbc.themes.LITERA)

