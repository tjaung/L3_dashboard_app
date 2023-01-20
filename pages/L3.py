import dash
from dash import html, dcc
from data_pull import MODELS_BY_PAL
from pprint import pprint
from pathlib import Path
import os
import explainerdashboard
from explainerdashboard import ExplainerDashboard, ExplainerHub, ClassifierExplainer

#dash.register_page(__name__, title='L3 Models List')

pages = Path.cwd() / "pages/L3_models"
pprint(os.listdir(pages))



layout = html.Div(children=[
    html.H1(children='L3 Models'),

    html.Div(children=[
        html.Div(
                html.A(
                    f"{PAL}", href=f"{pages}/{page}", target="_blank"
                )
            )
            for PAL, page in zip(MODELS_BY_PAL.keys(), os.listdir(pages))
        ]),

])
