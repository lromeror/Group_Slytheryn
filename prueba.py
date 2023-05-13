import dash_bootstrap_components as dbc
from dash import html

def cartas_jugador(name,cod_img,img_player,posicion):
    card = html.Button(
    dbc.Row(
        dbc.Col(
            html.H4(posicion),
        ),
        dbc.Col(html.Img(img_player))
    ),
    dbc.Row(html.H1('name')),
    dbc.Row(html.Img(cod_img)),className='carta_player_buttonm'
    )
    return card
L=[cartas_jugador(name,cod_img,img_player,'Delantero')]