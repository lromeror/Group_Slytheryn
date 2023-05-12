import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import server
from app import app
from pages import home,FIFA_WORLD_CUP_2022

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Inicio", href="/home"),
        dbc.DropdownMenuItem("FIFA WORLD CUP 2022", href="/FIFA_WORLD_CUP_2022"),
    ],
    nav = True,
    in_navbar = True,
    label = "Secciones",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/logo_espol.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("SLYTHERYN SOCCER DASHBOARD",)),
                    ],
                    align='center',
                    justify='center'

                ),
                href="/home",
                style={'width':'55vw'}
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
                style={'justifyContent':'flex-end',},
            ),
        ]
    ),
    style={'justifyContent':'spaceEvenly'},
    color="dark",
    dark=True,
    className="mb-4",
)


# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/FIFA_WORLD_CUP_2022':
        return FIFA_WORLD_CUP_2022.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)