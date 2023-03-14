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

hub = generate_dashes.generate_pages()
#hub.to_yaml(Path.cwd() / "hub.yaml", integrate_dashboard_yamls=True)
#hub = ExplainerHub.from_config(Path.cwd() / 'hub.yaml')

hub.run(host='0.0.0.0', port=9050, use_waitress=True)

# if __name__ == '__main__':
#     #hub.run()
