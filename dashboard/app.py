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

app = Dash(__name__, use_pages = False)

# hub = ExplainerHub([], title="Data Science Team L3 Models",
#             description="Dashboards for the Humana L3 Models created by the DS team.")

# model_dir = "/Users/tim.jaung/data_management/L3/SHAP/shap-app/modelFiles/Foot_Surgeries_Bunionectomy_and_Hammertoe"
# for pal in MODELS_BY_PAL.keys():
#     pal_file = pal.replace(' ', '_')
#     module = 'pages.L3_models.' + pal_file

#     if not os.path.exists(Path.cwd()/f'pages/L3_models/{pal_file}'):
#         print(f'Generating dashboard for {pal}...')
#         generate_dashes.generate_pages(pal)
#         print('Done')

#     Y = getattr(importlib.import_module(module), 'db')
#     hub.add_dashboard(Y)

hub = generate_dashes.generate_pages()

# authentication
#hub.add_user("cohere_user", "show_m3_the_$")

hub.run()


if __name__ == '__main__':
    app.run_server(debug=True)