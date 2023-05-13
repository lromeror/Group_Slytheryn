import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app

# change to app.layout if running as single page app instead
layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H1("Welcome to the Slytheryn Soccer dashboard", className="title",)]
                    , className="Container_text_frase",style={'margin-bottom':'4vw'},)
        ]),
    ])
])

