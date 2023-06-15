import dash_bootstrap_components as dbc
from dash import Dash, html,dash_table
import os
import pandas as pd
import numpy as np
import plotly.express as px


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

def card_info(country,name,i,DATAS_DIR):
    L=['games','goals','assists','possession','avg_age','cards_yellow','cards_red','confe']
    df = pd.read_csv(os.path.join(DATAS_DIR, "data_teamsCup.csv"),sep=",")
    selecciones = pd.read_csv(os.path.join(DATAS_DIR, "selecciones.csv"),sep=",")
    df = df[df['team'] == country]
    df['confe'] = [selecciones[selecciones.seleccion==team]['continente'] for team in df.team]
    if i==3:
        df['possession'] = (df['possession'].astype(str))+"%"
    div_info = dbc.Col(
    html.Div(
        [
            html.H2(f"{name.title()}"),
            html.Hr(className="my-2"),
            html.H4(df[L[i]].values[0]),
        ],
        className="h-100 p-5 text-black bg-light rounded-3 margin_div",
    ),
    md=3 ,className="text"
)
    return div_info
def row_card_info(country,lista,i,DATAS_DIR ):
    
    row_card = dbc.Container([
    dbc.Row([
        card_info(country,lista[i],i,DATAS_DIR),
        card_info(country,lista[i+1],i+1,DATAS_DIR),
        card_info(country,lista[i+2],i+2,DATAS_DIR),
        card_info(country,lista[i+3],i+3,DATAS_DIR),  
    ],className="container_row_card"),
    dbc.Row([
        card_info(country,lista[i+4],i+4,DATAS_DIR),
        card_info(country,lista[i+5],i+5,DATAS_DIR), 
        card_info(country,lista[i+6],i+6,DATAS_DIR),   
        card_info(country,lista[i+7],i+7,DATAS_DIR), 
    ],className="container_row_card")
])
    return row_card
def row_matches(DATAS_DIR,IMAGES_DIR,Id_team,goles_1,goles_2):
    selecciones = pd.read_csv(os.path.join(DATAS_DIR, "selecciones.csv"),sep=",")
    cod_img1 = (selecciones[selecciones.seleccion==Id_team[0]].reset_index()['cod_img'][0])+".png"
    cod_img2 = (selecciones[selecciones.seleccion==Id_team[1]].reset_index()['cod_img'][0])+".png"
    row_match = dbc.Row([
        dbc.Col([html.Img(src=os.path.join(IMAGES_DIR,cod_img1),className='img-fluid img-thumbnail img_country')],className="component"),
        dbc.Col(html.H3(f"{goles_1}           vs             {goles_2}"),className="result component"),
        dbc.Col([html.Img(src=os.path.join(IMAGES_DIR,cod_img2),className='img-fluid img-thumbnail img_country')],className="component"),
    ],className="bg-light match")
    return row_match

def created_row_matches(country,DATAS_DIR,IMAGES_DIR):
    df = pd.read_csv(os.path.join(DATAS_DIR,'Matches.csv'),sep=",")
    df = df[(df['1'] == country) | (df['2'] == country)]
    df  = df.rename(columns={'1_goals':'goals1','2_goals':'goals2'})
    df['1_goals'] = [x.split(',')[0] for x in df.score]
    df['2_goals'] = [x.split(',')[1] for x in df.score]
    df = df[['1','2','1_goals','2_goals']]
    df = df.reset_index(drop=True)
    created_row_matches_4 =dbc.Container([])
    created_row_matches_3 = created_row_matches_4
    created_row_matches_5=created_row_matches_4
    created_row_matches_6=created_row_matches_4
    df_1 = pd.read_csv(os.path.join(DATAS_DIR,'group_stats.csv'),sep=",")
    df3 = df_1[['group','team','matches_played','wins','draws','losses','goals_scored','goals_against','goal_difference','points']]
    df3.columns =['group','Team','PJ','G','E','L','GF','GC','DG','PTS']
    group_id = df3.loc[df3.Team==country]['group'].values[0]
    table = df3[df3['group']==group_id]
    table.drop("group",axis=1,inplace=True)
    title = html.H3("GROUP STAGE")
    created_row_matches_ = dbc.Container([
        row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][i],df['2'][i]],df['1_goals'].tolist()[i],df['2_goals'].tolist()[i])
        for i in range(3)
        ])
    tables1= dash_table.DataTable(
                            id='table_materias',
                            columns=[{'name':col, 'id':col}for col in table.columns],
                            data=table.to_dict('records'),  # the contents of the table
                            cell_selectable=True,  # para que no se me presente el hover
                            fill_width=False,
                            sort_action='native',
                            style_as_list_view=True,
                            style_header={
                                'backgroundColor': '#edf3f4',
                                'fontWeight': 'bold',
                                'textAlign': 'center'
                            },
                            style_cell={
                                'backgroundColor': '#edf3f4',
                                'textAlign': 'center',
                                'padding': '5px',
                                'textAlign': 'center'
                            },
                            style_data={'borderBottom': '1px solid #167ac6',
                                        'fontFamily': 'Quicksand'},
                            style_data_conditional = [
                                {
                                    'if': {
                                        'filter_query': '{{Team}} = {}'.format(country),
                                        },
                                    'backgroundColor': '#4a98d0',
                                    'fontWeight': 'bold'
                                }])            
    if len(df)>3:
        created_row_matches_3 = dbc.Container([
        dbc.Row([html.H3("Round of 16".title())],className='Container_principal margin2'),
        row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][3],df['2'][3]],df['1_goals'].tolist()[3],df['2_goals'].tolist()[3])
        ])
    if len(df)>4:
        created_row_matches_4 = dbc.Container([
        dbc.Row([html.H3("Quarter final".title())],className='Container_principal'),
        row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][4],df['2'][4]],df['1_goals'].tolist()[4],df['2_goals'].tolist()[4])
        ])
    if len(df)>5:
        created_row_matches_5 = dbc.Container([
        dbc.Row([html.H3("Semi-final".title())],className='Container_principal'),
        row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][5],df['2'][5]],df['1_goals'].tolist()[5],df['2_goals'].tolist()[5])
        ])
    if len(df)>6:
        if country not in ['Croatia','Morocco']:

            created_row_matches_6 = dbc.Container([
            dbc.Row([html.H3("Final".title())],className='Container_principal'),
            row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][6],df['2'][6]],df['1_goals'].tolist()[6],df['2_goals'].tolist()[6])
            ])
        else:
            created_row_matches_6 = dbc.Container([
            dbc.Row([html.H3("Play-off for third place".title())],className='Container_principal'),
            row_matches(DATAS_DIR,IMAGES_DIR,[df['1'][6],df['2'][6]],df['1_goals'].tolist()[6],df['2_goals'].tolist()[6])
            ])
    final = dbc.Container([title,created_row_matches_,tables1,created_row_matches_3,created_row_matches_4,created_row_matches_5,created_row_matches_6],className="Container_principal")
    return final

def createTop5(DATAS_DIR,country):
    dff= pd.read_csv(os.path.join(DATAS_DIR, "player_stats.csv"),sep=",")
    dff.replace("Saudi Arabia","Saudi_Arabia",inplace=True)
    df = dff[dff.team==country].sort_values(["goals"],ascending=False)
    df_asistidores = df[["player","assists","games"]][0:5]
    df_goleadores = df[["player","goals","games"]][0:5]
    title_top = dbc.Row([html.H5("Top 5 goal scorers".title())],className='title_Table')
    title_assis = dbc.Row([html.H5("Top 5 soccer assistants".title())],className='title_Table')
    table =dash_table.DataTable(
                            id='table_materias',
                            columns=[{'name':col, 'id':col}for col in df_goleadores.columns],
                            data=df_goleadores.to_dict('records'),  # the contents of the table
                            cell_selectable=True,  # para que no se me presente el hover
                            fill_width=False,
                            sort_action='native',
                            style_as_list_view=True,
                            style_header={
                                'backgroundColor': '#edf3f4',
                                'fontWeight': 'bold',
                                'textAlign': 'center'
                            },
                            style_cell={
                                'backgroundColor': '#edf3f4',
                                'textAlign': 'center',
                                'padding': '5px',
                                'textAlign': 'center'
                            },
                            style_data={'borderBottom': '1px solid #167ac6',
                                        'fontFamily': 'Quicksand'})
    table2 =dash_table.DataTable(
                            id='table_materias',
                            columns=[{'name':col, 'id':col}for col in df_asistidores.columns],
                            data=df_asistidores.to_dict('records'),  # the contents of the table
                            cell_selectable=True,  # para que no se me presente el hover
                            fill_width=False,
                            sort_action='native',
                            style_as_list_view=True,
                            style_header={
                                'backgroundColor': '#edf3f4',
                                'fontWeight': 'bold',
                                'textAlign': 'center'
                            },
                            style_cell={
                                'backgroundColor': '#edf3f4',
                                'textAlign': 'center',
                                'padding': '5px',
                                'textAlign': 'center'
                            },
                            style_data={'borderBottom': '1px solid #167ac6',
                                        'fontFamily': 'Quicksand'})
    final = dbc.Container([
        dbc.Col([title_top,table],className="margin3"),
        dbc.Col([title_assis,table2],className="margin3")],className="container_tables")
    return final

def top5player_goals (df,country):
    df_country = df[df.team==country]
    df_sorted = df_country.sort_values(by="goals", ascending=False).iloc[:5]

    fig_goals = px.bar(df_sorted, x='player', y=['goals_pens', 'pens_made'],
                barmode='stack', template='simple_white')

    fig_goals.update_layout(
        title='Top 5 players with most goals',
        xaxis_title='Players',
        yaxis_title='Goals'
    )
    return fig_goals


