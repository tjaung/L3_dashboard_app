
from pathlib import Path
import explainerdashboard
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard
import pickle
import dill
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_Diagnostic_cardiac_imaging_ECHO_dashboard():
    model_dir = str(Path.cwd() / "modelFiles/Diagnostic_cardiac_imaging_ECHO")
    #joblib_file = model_dir + "/Diagnostic_cardiac_imaging_ECHO.joblib"
    dill_file = model_dir + "/Diagnostic_cardiac_imaging_ECHO.dill"
    #yaml_file = model_dir + "/Diagnostic_cardiac_imaging_ECHO_dashboard.yaml"

    clas_explainer = ClassifierExplainer.from_file(dill_file)

    return clas_explainer

#author = MODELS_BY_PAL['Diagnostic cardiac imaging ECHO']['author']

db = ExplainerDashboard(get_Diagnostic_cardiac_imaging_ECHO_dashboard(), 
    title='Diagnostic cardiac imaging ECHO', 
    name='Diagnostic_cardiac_imaging_ECHO',
    logins = [['cohere-user', 'show_m3_the_$']],
    description="CARDIO L3 Model",
    bootstrap=dbc.themes.LITERA)

