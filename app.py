from backend.data_pull import MODELS_BY_PAL
import backend.generate_dashes as generate_dashes

from explainerdashboard import ClassifierExplainer, ExplainerDashboard, ExplainerHub
from dash import Dash
from flask import Flask
import dash_bootstrap_components as dbc
import plotly.express as px
from pathlib import Path
import os.path
import importlib


app = Flask(__name__)

#hub = generate_dashes.generate_pages()
#hub.to_yaml("hub.yaml", integrate_dashboard_yamls=True)
hub = ExplainerHub.from_config('hub.yaml')
app = hub.flask_server()

# if __name__ == '__main__':
#     #hub.run()
#     app.run_server(debug=True)