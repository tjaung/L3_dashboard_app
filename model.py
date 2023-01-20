from unittest.mock import MagicMock
import sys
sys.modules["xgboost"] = MagicMock()

from pathlib import Path
from flask import Flask

import dash
from dash_bootstrap_components.themes import FLATLY, BOOTSTRAP # bootstrap theme
from explainerdashboard import *





pkl_dir = Path.cwd() / "pkls"

app = Flask(__name__)

clas_explainer = ClassifierExplainer.from_file(pkl_dir / "Foot_Surgeries_Bunionectomy_and_Hammertoe.joblib")
clas_dashboard = ExplainerDashboard(clas_explainer, 
                    title="L3: Footsurgeries, Bunionectomy, and Hammertoe", 
                    server=app, url_base_pathname="/classifier/", 
                    header_hide_selector=True)

index_app = dash.Dash(
    __name__, 
    server=app, 
    url_base_pathname="/", 
    external_stylesheets=[BOOTSTRAP])

index_app.title = 'explainerdashboard'
index_app.layout = index_layout
register_callbacks(index_app)

@app.route("/")
def index():
    return index_app.index()

@app.route('/classifier')
def classifier_dashboard():
    return clas_dashboard.app.index()
