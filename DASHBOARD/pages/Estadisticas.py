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
from .Functions import div_countries, country_flag_name, Lineup_players,row_card_info,created_row_matches,row_matches,createTop5,top5player_goals
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
title_ = dbc.Row([html.H2("Stadistics".upper())],className="title_stadistics")


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
        games_title = dbc.Row([html.H2("GAMES")],className="title_stadistics")
        row_matches_all = created_row_matches(country,DATAS_DIR,IMAGES_DIR)
        div_goals = dbc.Container([
            dbc.Row(html.H4("GOALS and ASSISTS")),
            dbc.Row([createTop5(DATAS_DIR,country)])],className="Container_principal")
        
        df_ply = pd.read_csv(os.path.join(DATAS_DIR,'player_stats.csv'),sep=",")
        df_ply.replace("Saudi Arabia","Saudi_Arabia",inplace=True)
        df_country = df_ply[df_ply.team==country]
        print(country)
        #x =row_matches(DATAS_DIR,IMAGES_DIR,["Argentina","Mexico"],"2","3")
        df_sorted = df_country.sort_values(by="goals", ascending=False).iloc[:5]
        df_sorted=df_sorted.rename(columns={'goals_pens':'Goals' ,'pens_made':'Penals'})
        fig_goals = px.bar(df_sorted, x='player', y=['Goals', 'Penals'],
                        barmode='stack', template='simple_white',text_auto=True)
        fig_goals.update_layout(
                title='Top 5 players with most goals'.title(),title_x=0.5,
                xaxis_title='Players',
                yaxis_title='Goals',
                legend_title='TOTAL GOALS'
                
            )
        df_sorted1 = df_country.sort_values(by="assists", ascending=False).iloc[:5]

        fig_assist = px.bar(df_sorted1, x='player', y='assists',
                            template='simple_white',text_auto=True)
        fig_assist.update_traces(marker_color='rgb(46, 134, 193 )')
        fig_assist.update_layout(
            title='Top 5 players with most assists'.title(),title_x=0.5,
            xaxis_title='Players',
            yaxis_title='Assists',
        )
        matches_fifa_wc2022=pd.read_csv(os.path.join(DATAS_DIR,'Matches.csv'),sep=",")
        df_match = matches_fifa_wc2022[['match_no','1','2','1_poss','2_poss']]
        df_match.replace("Saudi Arabia","Saudi_Arabia",inplace=True)
        df_match = df_match[(df_match['1'] == country) | (df_match['2'] == country)]
        L=[]
        for x,y,poss1,poss2  in zip(df_match['1'],df_match['2'],df_match['1_poss'],df_match['2_poss']) :
            if x == country:
                L.append(poss1)
            else:
                L.append(poss2)
        df_poss_match = pd.DataFrame(columns=["Match","Possession"])
        df_poss_match['Match'] =np.arange(1,len(df_match)+1)
        df_poss_match['Possession'] = L
        df_poss_match['Possession']=df_poss_match['Possession'].astype(int)
        fig1 = px.bar(x=df_poss_match['Match'], y=df_poss_match['Possession'],text=[str(x)+"%" for x in df_poss_match['Possession']])
        fig1.update_traces(marker_color='rgb(46, 134, 193 )')
        fig1.update_layout(
            title=f'{country} Possession in each match'.title(),title_x=0.5,
            xaxis_title='Match',
            yaxis_title='Possession')
        fig1
        div_fig_goals_country= dbc.Container([
            dbc.Row([dcc.Graph(figure=fig_goals)],className='margin4'),
            dbc.Row([dcc.Graph(figure=fig_assist)],className='margin4'),
            dbc.Row([dcc.Graph(figure=fig1)],className='margin4'),
            ])
    return  container_per_country_c,title_,row_cards_info,games_title,row_matches_all,div_goals,div_fig_goals_country


layout = html.Div(
    [navbar,navbar2,user_country,countries,stadistics_country],className="Principal"

)

