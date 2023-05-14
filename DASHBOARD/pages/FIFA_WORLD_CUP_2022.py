import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html,callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("FIFA WORLD CUP 2022 ", className="text-center")
                    , className="mb-5 mt-5")
        ]),
    ])
])


