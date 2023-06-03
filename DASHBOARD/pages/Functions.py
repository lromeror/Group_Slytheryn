import dash_bootstrap_components as dbc
from dash import Dash, html
import os 

def country_flag(IMAGES_DIR,Id_team):
    country_flag = dbc.Col([html.Img(src=os.path.join(IMAGES_DIR,Id_team))],md=1)
    return country_flag

def rows_countries_flags(IMAGES_DIR,Id_team,list_id_images):   
    rows_countries = dbc.Row([
    country_flag(IMAGES_DIR,Id_team[list_id_images[0]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[1]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[2]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[3]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[4]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[5]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[6]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[7]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[8]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[9]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[10]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[11]])])
    return  rows_countries

def rows_countries_flags_last(IMAGES_DIR,Id_team,list_id_images):   
    rows_countries = dbc.Row([
    country_flag(IMAGES_DIR,Id_team[list_id_images[0]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[1]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[2]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[3]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[4]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[5]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[6]]),
    country_flag(IMAGES_DIR,Id_team[list_id_images[7]])])
    return  rows_countries

def div_countries (IMAGES_DIR,Id_team,list_list_id_images):
    div_countries = dbc.Container([
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[0]),
        rows_countries_flags(IMAGES_DIR,Id_team,list_list_id_images[1]),
        rows_countries_flags_last(IMAGES_DIR,Id_team,list_list_id_images[2])
    ])