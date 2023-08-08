import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, ctx
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os
import pandas as pd 
import numpy as np
import random as rd
import plotly.express as px
import plotly.graph_objects as go
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
                href="http://127.0.0.1:8050/",
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
navbar2 = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Home",href= "http://127.0.0.1:8050/",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Statistics",href= "/Estadisticas",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Comparations",href= "/Comparations",style={"textDecoration": "none"})),
                        #dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"),className="right"),
                        
                    ],
                    align="right",
                    className="g-0",
                ),
                #href="https://plotly.com",
                #style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=50),
            dbc.Collapse(
                id="navbar-collapse1",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)
PAGES_DIR = os.path.dirname(__file__)
APP_DIR = os.path.relpath(os.path.dirname(PAGES_DIR))
ASSETS_DIR = os.path.relpath(os.path.join(APP_DIR,'assets'))
DATAS_DIR = os.path.relpath(os.path.join(ASSETS_DIR,'datas'))
df_img_team = pd.read_csv(os.path.join(DATAS_DIR, "selecciones.csv"),sep=",")
list_teams = df_img_team.seleccion.tolist()
PLAYER_DIR  = '../assets/Images'
IMAGES_DIR = '../assets/Selecciones'

Selections_Teams = dbc.Container([
    dbc.Row(html.H2("CHOOSE TWO COUNTRIES"),className="Titlecenter"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(list_teams,"Argentina",id='country1'),
            ]),
        dbc.Col([
            dcc.Dropdown(list_teams,"Francia",id='country2')]
                ),
    ],className=""),
])
Images_Teams = dbc.Container([
    html.H1("hola"),
    dbc.Row(id="country"),
    ])

@callback(
    Output('ImgCountry1','children'),
    [Input('country','value')],
    [Input('country2','value')]
)
def getselectedteams(country1,country2): 
    cod_img = df_img_team[df_img_team['seleccion']==country1]['team']
    cod_img2 = df_img_team[df_img_team['seleccion']==country2]['team']
    confe = df_img_team[df_img_team['seleccion']==country1]["continente"]
    return dbc.Container([
            dbc.Col(html.Img(src=os.path.join(IMAGES_DIR,cod_img))),
            dbc.Col(html.Img(src=os.path.join(IMAGES_DIR,cod_img2))),
            ])


layout = html.Div(
    [navbar,navbar2,Selections_Teams,Images_Teams],className="Principal"
)
