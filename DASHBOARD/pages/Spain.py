pais='Spain'
import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html,callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import os 



# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py

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
df_img_team = pd.read_csv('DASHBOARD/assets/datas/selecciones.csv',sep=';')
cod_img = df_img_team[df_img_team['seleccion']==pais]['team'].values[0]
folder_img_players = f'assets/Images/{pais}'
folder_img_seleccion = f'assets/Selecciones'
players = pd.read_excel('DASHBOARD/assets/datas/Selecciones_mundial2022.xlsx',sheet_name=f'{pais}')
players.replace('Mediocampista','Mediocampo',inplace=True)
def cartas_jugador(name,cod_img,posicion):
    card = html.Div([
    html.Button([
    html.Div(
        [html.P(posicion)],className='text_pos'
    ),
    html.Div([html.Img(src=os.path.join(folder_img_players,name+'.png'),className='img_player')],className=''),
    html.Div([html.P(name)],className='text_name'),
    html.Div([html.Img(src=os.path.join(folder_img_seleccion,cod_img),className='img_team')],className='')
    ],className='button col d-flex align-items-md-stretch ')],className='carta_player_button')
    return card

layout = html.Div([
    html.Div(
    [navbar]),
    html.Div([
        html.Div([
            html.H4(f'{pais.upper()}'),
            html.Img(src= f'assets/Selecciones/{cod_img}'),
            html.H4('PLANTILLA')
        ],className='div_container_selec')
    ],className='container_selec'),
    html.Div([
        cartas_jugador(players.Jugador[0],cod_img,players.Posición[0]),
        cartas_jugador(players.Jugador[1],cod_img,players.Posición[1]),
        cartas_jugador(players.Jugador[2],cod_img,players.Posición[2]),
        cartas_jugador(players.Jugador[3],cod_img,players.Posición[3]),
        cartas_jugador(players.Jugador[4],cod_img,players.Posición[4]),
        cartas_jugador(players.Jugador[5],cod_img,players.Posición[5]),
        cartas_jugador(players.Jugador[6],cod_img,players.Posición[6]),
        cartas_jugador(players.Jugador[7],cod_img,players.Posición[7]),
        cartas_jugador(players.Jugador[8],cod_img,players.Posición[8]),
        cartas_jugador(players.Jugador[9],cod_img,players.Posición[9]),
        cartas_jugador(players.Jugador[10],cod_img,players.Posición[10]),
        cartas_jugador(players.Jugador[11],cod_img,players.Posición[11]),
        cartas_jugador(players.Jugador[12],cod_img,players.Posición[12]),
        cartas_jugador(players.Jugador[13],cod_img,players.Posición[13]),
        cartas_jugador(players.Jugador[14],cod_img,players.Posición[14]),
        cartas_jugador(players.Jugador[15],cod_img,players.Posición[15]),
        cartas_jugador(players.Jugador[16],cod_img,players.Posición[16]),
        cartas_jugador(players.Jugador[17],cod_img,players.Posición[17]),
        cartas_jugador(players.Jugador[18],cod_img,players.Posición[18]),
        cartas_jugador(players.Jugador[19],cod_img,players.Posición[19]),
        cartas_jugador(players.Jugador[20],cod_img,players.Posición[20]),
        cartas_jugador(players.Jugador[21],cod_img,players.Posición[21]),
        cartas_jugador(players.Jugador[22],cod_img,players.Posición[22]),
        cartas_jugador(players.Jugador[23],cod_img,players.Posición[23]),
        cartas_jugador(players.Jugador[24],cod_img,players.Posición[24]),
        cartas_jugador(players.Jugador[25],cod_img,players.Posición[25]),
        cartas_jugador(players.Jugador[26],cod_img,players.Posición[26]),
        ],className='row container_plantilla')
])
