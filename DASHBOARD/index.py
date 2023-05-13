import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import os 
from app import server
from app import app
from pages import home,FIFA_WORLD_CUP_2022,Argentina, Australia,Belgium,Brazil,Canada,Cameroon,Costa_Rica,Croatia, Denmark, Ecuador,England,España,France,Germany,Ghana,Iran,Japan,Korea_Republic,Saudi_Arabic,Marocco,Mexico,Netherlands,Polond,Portugal,Qatar,Senegal,Serbia,Switzerland,Tunisia,Uruguay,United_States,Wales,Confederations
"""
# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py

nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))
app = Dash(__name__, use_pages=True)



PLOTLY_LOGO = "https://cdn.cookielaw.org/logos/a22264f8-9d14-4ab8-ab4b-a61925d0e901/6b589592-a31b-4ede-9440-c6368b1eb13b/d0426540-ceee-4ccb-b321-ac2656d493bb/fcm_rgbf_s.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("", className="ms-2")),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="https://www.fifa.com/es",
                style={"textDecoration": "none"},
            ),
            html.A(
                dbc.Row(
                    [
                        html.P('CONFEDERATIONS'),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="pages/Confederations",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="#FFD500",
    dark=True,
)


@app.callback(
    Output("navbar-collapse", "is_open",),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
        {"key": "2", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
        {"key": "3", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
    ],
    controls=True,
    indicators=True,
    interval=2000,
    ride="carousel"
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
    [navbar]),
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
                [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Argentina':
        return Argentina.layout
    elif pathname == '/Confederations':
        return Confederations.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)"""