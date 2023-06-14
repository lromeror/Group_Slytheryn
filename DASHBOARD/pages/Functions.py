import dash_bootstrap_components as dbc
from dash import Dash, html
import os
import pandas as pd
import numpy as np

def country_flag(IMAGES_DIR,Id_team):
    country_flag = dbc.Col(dbc.Button(
                            [html.Img(src=os.path.join(IMAGES_DIR,Id_team),className='img-fluid img-thumbnail')],
                            id = Id_team.split('.')[0],
                            className="btn btn-link btn_back"),
                            )
    return country_flag

def rows_countries_flags(IMAGES_DIR,Id_team,list_id_images):  
    
    rows_countries = dbc.Container(
        [dbc.Row([
        country_flag(IMAGES_DIR,Id_team[list_id_images[0]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[1]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[2]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[3]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[4]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[5]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[6]]),
        country_flag(IMAGES_DIR,Id_team[list_id_images[7]]),
        ])]
    )
    return  rows_countries

def div_countries (IMAGES_DIR,Id_team,list_list_id_images):
    div_countries = dbc.Container([
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[0]),
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[1]),
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[2]),
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[3])
    ])
    return div_countries

def country_flag_name(pais,cod_img,IMAGES_DIR):
    country_flag_name_c = dbc.Container([
        dbc.Container([
            html.H4(f'{pais.upper()}'),
            html.Img(src= os.path.join(IMAGES_DIR,cod_img),className='images_flag'),
            html.H4('PLAYERS')
        ],className='div_container_selec')
    ],className='container_selec'),
    return country_flag_name_c


def cartas_jugador(name,cod_img,posicion,folder_img_players,folder_img_seleccion):
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

def cartas_jugador_polonia(name,cod_img,posicion,folder_img_players,folder_img_seleccion):
    card = html.Div([
    html.Button([
    html.Div(
        [html.P(posicion)],className='text_pos'
    ),
    html.Div([html.Img(src=os.path.join(folder_img_players,name+'.png'),className='img_player')],className=''),
    html.Div([html.P(name)],className='text_name_po'),
    html.Div([html.Img(src=os.path.join(folder_img_seleccion,cod_img),className='img_team')],className='')
    ],className='button col d-flex align-items-md-stretch ')],className='carta_player_button')
    return card

def cartas_jugador_dominguez(name,cod_img,posicion,folder_img_players,folder_img_seleccion):
    card = html.Div([
    html.Button([
    html.Div(
        [html.P(posicion)],className='text_pos'
    ),
    html.Div([html.Img(src=os.path.join(folder_img_players,name+'.png'),className='img_player')],className=''),
    html.Div([html.P(name)],className='text_name_do'),
    html.Div([html.Img(src=os.path.join(folder_img_seleccion,cod_img),className='img_team')],className='')
    ],className='button col d-flex align-items-md-stretch ')],className='carta_player_button')
    return card

def Lineup_players(cod_img,country,DATAS_DIR,triggered_id,IMAGES_DIR,PLAYER_DIR):
    folder_img_players = os.path.join(PLAYER_DIR,country)
    folder_img_seleccion = IMAGES_DIR
    players = pd.read_csv(os.path.join(DATAS_DIR, "Selecciones_22.csv"),sep=",")
    players = players[players.PAIS==country].reset_index()
    
    if country == "Cameroon":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [1,3,17,22,25]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
        
    elif country == 'Costa Rica':
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [3,26]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country == 'Korea Republic':
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [1,26]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country in ['France','Iran']:
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(25)
                ],className='row container_plantilla')
        ])

    elif country=="Polonnd":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [6,13,16,19,22,26]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country=="Uruguay":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [20]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
    elif country=="Serbia":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [0,18]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
    elif country =="England":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [9,21]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country=="Switzerland":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [21]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country == "Saudi_Arabia":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [1,2,22]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
    elif country=="Ecuador":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [1]
                else cartas_jugador_dominguez(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])

    elif country=="Morocco":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [2,24]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
    
    elif country == "Ghana":
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                if x not in [1]
                else cartas_jugador_polonia(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
    else:
        div_prin = html.Div([
            html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
            html.Div([
                cartas_jugador(players.Jugador[x],cod_img,players.Posición[x],folder_img_players,folder_img_seleccion)
                for x in range(26)
                ],className='row container_plantilla')
        ])
        
    return div_prin
