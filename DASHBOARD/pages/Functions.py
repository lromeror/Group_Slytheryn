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
            html.H4('PLANTILLA')
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
def Lineup_players(cod_img,country,DATAS_DIR,triggered_id,IMAGES_DIR,PLAYER_DIR):
    folder_img_players = os.path.join(PLAYER_DIR,country)
    folder_img_seleccion = IMAGES_DIR
    players = pd.read_csv(os.path.join(DATAS_DIR, "Selecciones_22.csv"),sep=",")
    players=players[players.PAIS==country].reset_index()
    div_prin = html.Div([
        html.Div(country_flag_name(country,triggered_id+".png",IMAGES_DIR)),
        html.Div([
            cartas_jugador(players.Jugador[0],cod_img,players.Posición[0],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[1],cod_img,players.Posición[1],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[2],cod_img,players.Posición[2],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[3],cod_img,players.Posición[3],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[4],cod_img,players.Posición[4],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[5],cod_img,players.Posición[5],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[6],cod_img,players.Posición[6],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[7],cod_img,players.Posición[7],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[8],cod_img,players.Posición[8],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[9],cod_img,players.Posición[9],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[10],cod_img,players.Posición[10],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[11],cod_img,players.Posición[11],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[12],cod_img,players.Posición[12],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[13],cod_img,players.Posición[13],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[14],cod_img,players.Posición[14],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[15],cod_img,players.Posición[15],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[16],cod_img,players.Posición[16],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[17],cod_img,players.Posición[17],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[18],cod_img,players.Posición[18],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[19],cod_img,players.Posición[19],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[20],cod_img,players.Posición[20],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[21],cod_img,players.Posición[21],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[22],cod_img,players.Posición[22],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[23],cod_img,players.Posición[23],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[24],cod_img,players.Posición[24],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[25],cod_img,players.Posición[25],folder_img_players,folder_img_seleccion),
            cartas_jugador(players.Jugador[26],cod_img,players.Posición[26],folder_img_players,folder_img_seleccion),
            ],className='row container_plantilla')
    ])
    return div_prin
