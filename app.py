from backend.data_pull import MODELS_BY_PAL
import backend.generate_dashes as generate_dashes

import explainerdashboard
from explainerdashboard import ClassifierExplainer, ExplainerDashboard, ExplainerHub
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from pathlib import Path
import os.path
import importlib
from flask import render_template

app = Dash(__name__, use_pages = False)

hub = generate_dashes.generate_pages()
hub.to_yaml("hub.yaml", integrate_dashboard_yamls=True)

hub.run()

""" 
if __name__ == '__main__':
    app.run_server(debug=True) """