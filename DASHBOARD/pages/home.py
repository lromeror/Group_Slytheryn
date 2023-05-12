import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app

# change to app.layout if running as single page app instead
layout = html.Div([
    html.Div([
        html.Div([
            html.Div(html.H1("Welcome to the Slytheryn Soccer dashboard", className="title",)
                    , className="Container_text_frase",style={'margin-bottom':'4vw'},)
        ]),
        html.Div([
            html.Div([
                html.Div([html.H5(children=' “El día que no disfrute en el campo, voy a dejar el futbol” ')], className="text_frase")
                ],className='Container_text_frase'),
            html.Div([
                html.Div([html.Img(src='https://emprendedor.com/wp-content/uploads/2022/12/lionel-messi-copa-del-mundo-3.jpg',alt='Messi',)],className='container_img'),
                html.Div([html.Img(src='https://pbs.twimg.com/media/FFnsNEmXwAcdSi-.jpg:large',alt='Messi2')],className='container_img'),
                html.Div([html.Img(src='https://studiofutbol.com.ec/wp-content/uploads/2023/05/messi-laureus.jpg',alt='Messi3')],className='container_img'),
                ],className='container_div_img'),
            html.Div([
                html.Div([html.H5(children=' “Al final, cuando se termine todo esto, ¿qué te llevas? Mi intención es que, cuando me retire, se me recuerde por ser buen tipo” - Leonel Messi ')], className="text_frase")
                ],className='Container_text_frase')
        ],className='frases_jugador'),
        html.Div([
            html.Div([
                html.Div([html.H5(children=' “Cuando la gente tiene éxito, es gracias al sacrificio. La suerte no tiene nada que ver con el éxito” ')], className="text_frase")
                ],className='Container_text_frase'),
            html.Div([
                html.Div([html.Img(src='https://i.ytimg.com/vi/yv_JvjGdi34/maxresdefault.jpg',alt='Messi',)],className='container_img'),
                html.Div([html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Maradona-Mundial_86_con_la_copa.JPG/1200px-Maradona-Mundial_86_con_la_copa.JPG',alt='Messi2')],className='container_img'),
                html.Div([html.Img(src='https://www.mundodeportivo.com/us/files/article_main_microformat/files/fp/uploads/2022/11/18/6377b9477bb99.r_d.369-213-0.png',alt='Messi3')],className='container_img'),
                ],className='container_div_img'),
            html.Div([
                html.Div([html.H5(children=' “Estoy arrepentido del 99 % de todo lo que hice en mi vida; pero el 1% que es el fútbol salva el resto” - Diego Maradona')], className="text_frase")
                ],className='Container_text_frase')
        ],className='frases_jugador'),
         html.Div([
            html.Div([
                html.Div([html.H5(children=' “La gente ve a los futbolistas como seres diferentes, como si fuéramos intocables, como si nunca nos pasara nada, pero somos personas.” ')], className="text_frase")
                ],className='Container_text_frase'),
            html.Div([
                html.Div([html.Img(src='https://d3h7g948tee6ho.cloudfront.net/wp-content/uploads/2018/04/iniesta-copas.jpg',alt='Messi',)],className='container_img'),
                html.Div([html.Img(src='https://www.sportzcraazy.com/wp-content/uploads/2019/09/Andres-Iniesta-bio-e1567665343886.jpg',alt='Messi2')],className='container_img'),
                html.Div([html.Img(src='https://cloudfront-us-east-1.images.arcpublishing.com/eluniverso/ZPO4LBYDOBGQZER4GGWFEEY6RE.jpg',alt='Messi3')],className='container_img'),
                ],className='container_div_img'),
            html.Div([
                html.Div([html.H5(children='“Juego para ser feliz, no para ganar nada” - Andrés Iniesta')], className="text_frase")
                ],className='Container_text_frase')
        ],className='frases_jugador')
    ],className='Container_frases_img')

])
