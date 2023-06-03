import dash_bootstrap_components as dbc
from dash import Dash, html
import os 

def country_flag(IMAGES_DIR,Id_team):
    country_flag = dbc.Col([html.Img(src=os.path.join(IMAGES_DIR,Id_team))],className='col-lg-6 col-md-6 col-sm-6 col-xs-12')
    return country_flag

def rows_countries_flags(IMAGES_DIR,Id_team,list_id_images):   
    rows_countries = dbc.Row([
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[0]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[1]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[2]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[3]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[4]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[5]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[6]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[7]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[8]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[9]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[10]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[11]])],md=1)])
    return  rows_countries

def rows_countries_flags_last(IMAGES_DIR,Id_team,list_id_images):   
    rows_countries = dbc.Row([
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[0]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[1]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[2]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[3]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[4]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[5]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[6]])],md=1),
        dbc.Col([country_flag(IMAGES_DIR,Id_team[list_id_images[7]])],md=1),
    ])
    return  rows_countries

def div_countries (IMAGES_DIR,Id_team,list_list_id_images):
    div_countries = dbc.Container([
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[0]),
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[1]),
        rows_countries_flags_last(IMAGES_DIR,Id_team,list_list_id_images[2])
    ])
    return div_countries