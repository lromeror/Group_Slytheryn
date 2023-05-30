import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os
import pandas as pd 
import numpy as np

nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))



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
            dcc.Link(
                dbc.Row(
                    [
                        html.P('CONFEDERATIONS'),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="/Confederations",
                style={"textDecoration": "none"},
            ),
            dcc.Link(
                dbc.Row(
                    [
                        html.P('ESTADISTICS'),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="/Estadisticas",
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
PAGES_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.dirname(PAGES_DIR))
ASSETS_DIR = os.path.join(APP_DIR,'assets')
DATAS_DIR = os.path.join(ASSETS_DIR,'datas')
IMAGES_DIR = os.path.join(ASSETS_DIR,'Selecciones')
print(IMAGES_DIR)
DIR= os.path.join(DATAS_DIR, "selecciones.csv")
df_img_team = pd.read_csv(DIR,sep=';')
Id_team = df_img_team['team'].tolist()

countries = dbc.Container([
    dbc.Row([
        dbc.Col([html.Img(src=os.path.join(IMAGES_DIR,Id_team[0]))],md=4),
    ])
])
print(os.path.join(IMAGES_DIR,Id_team[0]))

#folder=r"C:/Users/Jonanyu 11.1/Desktop/img"
#os.path.join(folder,"cm1.jpg")
layout = html.Div(
    [navbar,countries]
    #html.Img(children=os.path.join(folder,"cm1.jpg"))

)
