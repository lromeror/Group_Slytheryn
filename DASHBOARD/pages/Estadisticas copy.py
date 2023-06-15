import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, ctx
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os
import pandas as pd 
import numpy as np
import random as rd
from .Functions import div_countries, country_flag_name, Lineup_players,row_card_info,created_row_matches,row_matches
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
navbar2 = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Home",href= "/home1",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Confederations",href= "/Confederations",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Statistics",href= "/Estadisticas",style={"textDecoration": "none"})),
                        #dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"),className="right"),
                        
                    ],
                    align="right",
                    className="g-0",
                ),
                #href="https://plotly.com",
                #style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
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

user_country = dbc.Container([
    dbc.Row([
        html.H2('SELECTED COUNTRY ',style={'margin':'1vw  0 1vw  0'}),
    ])
])
PAGES_DIR = os.path.dirname(__file__)
APP_DIR = os.path.relpath(os.path.dirname(PAGES_DIR))
ASSETS_DIR = os.path.relpath(os.path.join(APP_DIR,'assets'))
DATAS_DIR = os.path.relpath(os.path.join(ASSETS_DIR,'datas'))
#DATAS_DIR = '../assets/datas'
PLAYER_DIR  = '../assets/Images'
IMAGES_DIR = '../assets/Selecciones'

df_img_team = pd.read_csv(os.path.join(DATAS_DIR, "selecciones.csv"),sep=",")
Id_team = df_img_team['team'].tolist()
list_list_id_images = [[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15],[16,17,18,19,20,21,22,23],[24,25,26,27,28,29,30,31]]
list_id_images = np.arange(0,32)

countries = dbc.Container([
    div_countries (IMAGES_DIR,Id_team,list_list_id_images)
    ])

stadistics_country = dbc.Container(
    id ='container_country',className="stadicts_country"
)
title_ = dbc.Row([html.H2("Stadistics")],className="title_stadistics")
@callback(
    Output('container_country','children'),
    [Input(f'{Id_team[0].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[1].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[2].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[3].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[4].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[5].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[6].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[7].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[8].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[9].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[10].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[11].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[12].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[13].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[14].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[15].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[16].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[17].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[18].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[19].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[20].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[21].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[22].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[23].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[24].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[25].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[26].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[27].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[28].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[29].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[30].split(".")[0]}','n_clicks')],
    [Input(f'{Id_team[31].split(".")[0]}','n_clicks')],
)
def container_per_country(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31):
    triggered_id = ctx.triggered_id
    #print(triggered_id)
    #pais = df_img_team[df_img_team['cod_img']==triggered_id]['seleccion']
    if triggered_id !=  None :
        country = df_img_team[df_img_team.cod_img==triggered_id]['seleccion'].values[0]
        cod_img = triggered_id+".png"
    abreviaturas = df_img_team['cod_img'].tolist()
    abreviaturas.append(None)
    pos = abreviaturas.index(triggered_id)
    if triggered_id ==  None:
        return html.H4(" ")
    elif triggered_id == abreviaturas[pos]:
        container_per_country_c = html.Div(Lineup_players(cod_img,country,DATAS_DIR,triggered_id,IMAGES_DIR,PLAYER_DIR))
        lista=['Games','Goals','Assists','Posession','Avg_age','Yellow Cards','Red Cards','Confederation']
        row_cards_info = row_card_info(country,lista,0,DATAS_DIR)
        games_title = dbc.Row([html.H2("Games")],className="title_stadistics")
        row_matches_all = created_row_matches(country,DATAS_DIR,IMAGES_DIR)
        #x =row_matches(DATAS_DIR,IMAGES_DIR,["Argentina","Mexico"],"2","3")
        return  container_per_country_c,title_,row_cards_info,games_title,row_matches_all


def graphics_player(country):
    df_ply = pd.read_excel(os.path.join(DATAS_DIR,'Players.xlsx'),sheet_name='player_stats')
    html.Div([
        
        dcc.Dropdown(
            df_ply[df_ply["team"]==country], id="player_d"
        ),
        dcc.Graph(id="player_g"),
    ])
    @callback(
        [Output("player_g", "figure")],
        Input("player_d", "value"))
    def update_bar_chart(player):
        indice = df_ply[df_ply["player"]==player].index
        df_player = df_ply.loc[indice, :]
        fig_games_player = px.bar(df_player, x = 'player', y =['games_starts', 'games_sub'],  color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_games_player.update_layout(template='simple_white', title=f'Total games played by {player}',
            xaxis_title='Team',
            yaxis_title='Games' )
        
        return fig_games_player
    
layout = html.Div(
    [navbar,navbar2,user_country,countries,stadistics_country],className="Principal"

)

