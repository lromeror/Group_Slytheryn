import plotly.express as px
import pandas as pd
import numpy as np

import dash
from dash import Dash, dcc, html, dash_table

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from app import app
import plotly.graph_objects as go

df = pd.read_excel('Dashboard/pages/RptPlanifHorarioExam_20230120.xlsx')

for c in df.columns:
   if df[c].nunique() == 1:
       df.drop(c, axis="columns", inplace=True)

df.drop(columns="EMAIL", inplace=True)

#df.groupby("CAMPUS").count().EXAMEN

df['HINICIO'] = df['HORAINICIO'].dt.hour.astype(object)
df['HFIN'] = df['HORAFIN'].dt.hour.astype(object)
#df[df["HORAINICIO"] == pd.to_datetime('1970-01-01 00:00:00').time]
df['MINICIO'] = df['HORAINICIO'].dt.minute.astype(object)
df['MFIN'] = df['HORAFIN'].dt.minute.astype(object)
df['HORAINICIO'] = df.FECHA + pd.to_timedelta(df.HINICIO, unit='h') + pd.to_timedelta(df.MINICIO, unit='m')
df['HORAFIN'] = df.FECHA + pd.to_timedelta(df.HFIN, unit='h') + pd.to_timedelta(df.MFIN, unit='m')

def add_day(row):
    if row['HORAINICIO'].hour == 0 and row['HORAINICIO'].minute == 0:
        return row['HORAFIN'] + pd.Timedelta(days=1)
    else:
        return row['HORAFIN']

df['HORAFIN'] = df.apply(add_day, axis=1)

df['EXAMEN'].replace('1','Parcial',inplace = True)
df['EXAMEN'].replace('2','Final',inplace = True)
df['EXAMEN'].replace('M','Mejoramiento',inplace = True)

fechas=list(df['FECHA'].value_counts().index.sort_values())
dia_fecha=[]
for fecha in  fechas:
  dia= df[df['FECHA']==fecha].reset_index()['DIA'][0]
  dia_fecha.append(dia)
for i in range(df.shape[0]):
  fecha=df['FECHA'][i]
  di=df['DIA'][i]
  indi_fecha= fechas.index(fecha)
  if di != dia_fecha[indi_fecha]:
    df['DIA'][i] = dia_fecha[indi_fecha]

lol = df.groupby(['NOMBRE','PARALELO']).count().reset_index()
masters = lol[lol['EXAMEN'] == 2].NOMBRE.unique()
practandmooc = lol[lol['EXAMEN'] == 1].NOMBRE.unique()


for ind, row in df.iterrows():
    if np.isin(row[5], masters):
        df.loc[ind,'AREA'] = 'Posgrado'
    elif row[7] >= 100:
        df.loc[ind,'AREA'] = 'Otro'
    else:
        df.loc[ind,'AREA'] = 'Grado'


campusdf = df[df["CAMPUS"] == "CAMPUS GUSTAVO GALINDO"] #grado y pregrado
practcampusdf = df[df["CAMPUS"] == "CAMPUS GUSTAVO GALINDO"][df["PARALELO"] >= 100] #Moocs e investigación

block_occurrencies = campusdf[df.EXAMEN == 'Parcial'].groupby('BLOQUE').count().reset_index().sort_values('FECHA', ascending = False).loc[:,'BLOQUE':'FECHA']


dias_es=['lunes','martes','miércoles','jueves','viernes']
dias_fds=['sábado','domingo']
mat_dias_es=df[df['DIA'].isin(dias_es)]
mat_dias_es.drop(index=range(3945,4061),inplace=True)
mat_dias_fds=df[df['DIA'].isin(dias_fds)]

Ex_U_es=mat_dias_es[mat_dias_es['EXAMEN']=='Final']
Ex_U_fds=mat_dias_fds[mat_dias_fds['EXAMEN']=='Final']
Ex_U=df[df['EXAMEN']=='Final']
#campusdf1 = campusdf[campusdf["EXAMEN"] == "1"]

faccolors=["#446038", "#11b0be", "#feda04", "#1b6cb3",
            "#59368a", '#dc2284', '#53ac33', "#7393a8", "#264067"]

layout = html.Div([
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.H1("CASA GRYFFINDOR", className="text-center"),
                            className="mb-5 mt-5")
                ]),]),
            dbc.Row([]),
            html.Div([html.H1('HORARIO DE EXÁMENES - II PAO 2022'),
                html.Div([
            html.H3('5 Bloques más ocupados (Examen Parcial)',style={'margin-top':'4vw'}),
            dash_table.DataTable(
                id = 'topbloques',
                columns = [{'name': col, 'id': col} for col in block_occurrencies.columns],
                data = block_occurrencies.head().to_dict('records')),
            html.Br(),

            html.H3('5 Bloques menos ocupados (Examen Parcial)',style={'margin-top':'4vw'}),
            dash_table.DataTable(
                id = 'lowbloques',
                columns = [{'name': col, 'id': col} for col in block_occurrencies.columns],
                data = block_occurrencies.sort_values('FECHA', ascending = True).head().to_dict('records')),
            html.Br(),

            html.Div([
                html.H2('Distribución de exámenes',style={'margin-top':'4vw'})
                    ]),

            html.Br(),
            #html.Div([
                    html.H2('Distribución de exámenes',style={'margin-top':'4vw'}),
                    html.Br(),
                    html.Div([
            dcc.Dropdown(
                id='dropdown_area',
                options=['Grado','Posgrado','Otro'],
                placeholder='Selecciona un área: ',
                clearable=False
            ),
            html.Br(),
            html.Div(id='output-div'),
                    ]),
                    html.P('Seleccione un tipo de examen:'),
                    dcc.Dropdown(
                        ['Parcial','Final','Mejoramiento'],
                        'Parcial',
                        id='dropdown_examen')
                    ],style={'margin-top':'2vw'}),
                html.Div([
                    html.P('Seleccione un bloque de edificios: '),
                    dcc.Dropdown(np.sort(campusdf.BLOQUE.unique()),
                            campusdf.BLOQUE.unique()[0],
                            id = 'dropdown_bloques')
                        ],style = {'margin-top':'2vw'})
                ],style = {'margin':'2vw'}),
            html.Div([
                dcc.Graph(id='graph_timeline')],style={'margin':'2vw'}),
            html.Div([
                html.H2('Detalles de las materias',style={'margin-top':'4vw'}),
                html.Div([
                    html.Div([
                        html.P('Seleccione el Campus :'),
                        dcc.Dropdown(
                            df.CAMPUS.unique(),
                            'CAMPUS GUSTAVO GALINDO',
                            id='dropdown_campus_treemap',)],style={'margin-top':'2vw','width':'35vw'})
                        , html.Div([        
                            html.P('Facultades Disponibles :'), 
                            dcc.Dropdown(id='dropdown_facultades_treemap')],style={'margin-top':'2vw','width':'45vw'})],style={'display':'flex','justify-content':'space-between','align-items':'center'})
                , html.Div([        
                            html.P('Materias Disponibles :'), 
                            dcc.Dropdown([],id='dropdown_materias_disp_treemap')],style={'margin-top':'2vw'})
                , html.Div([
                            html.Div([
                            dcc.Graph(id='graph_treemap_mat')])
                            ],style={'margin':'2vw'})],style={'margin-top':'2vw','margin':'2vw'})
            , html.Div([
                
                html.Div([
                    html.Div([
                        html.Div([
                            html.P('Seleccione el Campus :'),
                            dcc.Dropdown(
                                df.CAMPUS.unique(),
                                'CAMPUS GUSTAVO GALINDO',
                                id='dropdown_campus_bloque_bar',)],style={'margin-top':'2vw','width':'25vw'})
                        , html.Div([        
                            html.P('Facultades Disponibles :'), 
                            dcc.Dropdown(id='dropdown_facultades_bloque_bar')],style={'margin-top':'2vw','width':'45vw'})
                        , html.Div([        
                            html.P('Bloques Disponibles :'), 
                            dcc.Dropdown(id='dropdown_bloque_bar')],style={'margin-top':'2vw','width':'20vw'})],style={'display':'flex','justify-content':'space-between','align-items':'center'})
                    ,html.Div([
                        html.P('Exámenes Disponibles :'), 
                        dcc.Dropdown(id='dropdown_examenes_bloque_bar')])])
                , html.Div([
                    html.Div([
                            dcc.Graph(id='graph_bloque_bar')])
                            
                    , html.Div([
                        html.Div( id='bloque_tabla'
                        )],style={'display':'flex','justify-content':'space-between','align-items':'center'})],style={'margin':'2vw','display':'flex','justify-content':'space-between'})
                ,html.Div([
                    html.P('Seleccione una Hora de Inicio'),
                    dcc.Dropdown(id='dropdown_hora')
                    ])
                ])

                        
            , html.Div([
                html.Div([
                    html.H2('Cantidad de examenes tomados por cada bloque',style={'margin-top':'4vw'})
                    , html.P('Seleccione una facultad:')
                    , dcc.Dropdown(
                        df.UNIDAD.unique(), 'Faculta de Ciencias Sociales y Humanísticas', id='select_facu')],style={'margin-top':'2vw'}
                    )
                , html.Div([
                    dcc.Graph(id='bars_facu')
                ])
                ])
            , html.Div([
                    html.H2('Distribución de docentes presentes en aulas por facultad')
                    , html.P('Seleccione facultad:')     
                    , dcc.Dropdown(
                        df.UNIDAD.unique(), 'Facultad de Ciencias Naturales y Matemáticas', id='select_facu2') 
                    ,html.Br()              
                    , dcc.Checklist(
                    id='checklist_figs',
                    options=[{'label': 'Boxplot', 'value': 'boxplot'},
                            {'label': 'Scatterplot', 'value': 'scatterplot'},
                            ],
                    value=['boxplot']
                )  
                , html.Div([
                    dcc.Graph(id='boxplot',style={'display': 'inline-block'})    
                    , dcc.Graph(id='scatterplot',style={'display': 'inline-block'})
                ], style={'margin-top':'2vw', 'display':'flex'})  
                , html.Div([ 
                    html.H2('Distribución de aulas por horario')
                    , dcc.Tabs(id="tabs-graph", 
                               children=[
                         dcc.Tab(label='Pregrado', value='pregrado_label', children=[
                             html.P('Seleccione Bloque:') 
                            ,dcc.Dropdown(Ex_U_es.BLOQUE.unique(),id='select_bloque1') ])
                        , dcc.Tab(label='Grado', value='grado_label', children=[
                            html.P('Seleccione Bloque:') 
                            ,dcc.Dropdown(Ex_U_fds.BLOQUE.unique(),id='select_bloque2') ])
                        ])
                    , html.Div(id='tabs-content-graph')   
                    ])
                ,html.Div([ 
                    html.H2('')        
                ])
                ,html.Br() 
                ,html.Br() 
                ,html.Br() 
                , html.Div([
                    html.P('DASH CASA GRYFFINDOR © 2023')],id="copyright",style={"display": "flex","justify-content": "center","align-items": "center"})
 
            ])
                
            ], style={"display": "flex", "flex-direction": "column",'margin':'4vw'})  
        



# @app.callback(Output('graph_timeline', 'figure'),
#     [Input('dropdown_examen', 'value'),
#     Input('dropdown_bloques', 'value')])   
# def update_figure(examen_selected,bloque_selected):
#     df_timeline = campusdf[(campusdf['BLOQUE'] == bloque_selected) & (campusdf['EXAMEN'] == examen_selected)]
#     fig_timeline = px.timeline(df_timeline, x_start = "HORAINICIO", x_end = "HORAFIN", y = "AULA",
#                         color = "UNIDAD", title="Distribución de aulas de éxamenes por bloque y por intervalos de tiempo.",
#                         hover_name = "NOMBRE")
#     return fig_timeline

# @app.callback(
#     Output('dropdown_facultades_treemap', 'options'),
#     Input('dropdown_campus_treemap', 'value'))
# def set_facultad_options(selected_campus):
#     df_camp = df[df['CAMPUS']==selected_campus]
#     return [{'label': i, 'value': i} for i in df_camp['UNIDAD'].unique()]

# @app.callback(
#     Output('dropdown_facultades_treemap', 'value'),
#    Input('dropdown_facultades_treemap', 'options'))
# def get_facultad_value(valor_prede):
#     return [k['value'] for k in valor_prede][0]

# @app.callback(
#     Output('dropdown_materias_disp_treemap', 'options'),
#     [Input('dropdown_facultades_treemap', 'value'),
#     Input('dropdown_campus_treemap', 'value')] )
# def set_materias_options(selected_facultad,selected_campus):
#     df_uni = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)]
#     return [{'label': i, 'value': i} for i in df_uni['NOMBRE'].unique()]

# @app.callback(
#     Output('dropdown_materias_disp_treemap', 'value'),
#    Input('dropdown_materias_disp_treemap', 'options'))
# def get_materia_value(v_prede):
#     return [k['value'] for k in v_prede][0]

# @app.callback(Output('graph_treemap_mat', 'figure'),
#     [Input('dropdown_campus_treemap', 'value'),
#     Input('dropdown_facultades_treemap', 'value'),
#     Input('dropdown_materias_disp_treemap', 'value')])
# def update_figure(selected_campus,selected_facultad,selected_materia):
#     df_materia_final=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)&(df['NOMBRE']==selected_materia)]
#     examenes = df_materia_final['EXAMEN'].unique()
#     i_df=0
#     df_materia_u = pd.DataFrame(columns=['NOMBRE','EXAMEN','TIPOPARALELO','PARALELO','NUMREGISTRADOS','BLOQUE','AULA','HORA','DATOS'])
#     for examen in examenes:
#         paralel = 'Teórico'
#         df_materia_ex = df_materia_final[df_materia_final['EXAMEN']==examen].reset_index()
#         fecha = str(df_materia_ex['FECHA'][0])[:11].replace('-','/')
#         dia = df_materia_ex['DIA'][0]
#         fecha_texto = f'Examen {examen} - {fecha} ({dia})'
#         print(fecha_texto)
#         p_teo = df_materia_ex[df_materia_ex['PARALELO']<100].reset_index()
#         for i in range(p_teo.shape[0]):
#             datos=[]
#             num_paralelo=p_teo['PARALELO'][i]
#             num_registros=p_teo['NUMREGISTRADOS'][i]
#             l_num_regis=f'Estudiantes Registrados: {num_registros}'
#             datos.append(l_num_regis)
#             aula=p_teo['AULA'][i]
#             bloque=p_teo['BLOQUE'][i]
#             l_bloque=f'Bloque: {bloque}'
#             datos.append(l_bloque)
#             l_aula=f'Aula: {aula}'
#             datos.append(l_aula)
#             hora1=str(p_teo['HORAINICIO'][i])[11:13]
#             hora2=str(p_teo['HORAFIN'][i])[11:13]
#             l_fecha= f'Hora del Exámen: {hora1} - {hora2} hrs'
#             datos.append(l_fecha)
#             df_materia_u.loc[i_df]=[selected_materia,fecha_texto,paralel,f'Paralelo {num_paralelo}',num_registros,bloque,aula,f'{hora1} - {hora2}','<br>'.join(datos)]
#             i_df+=1 
#         if df_materia_ex[df_materia_ex['PARALELO']>=100].shape[0] >0:
#             p_practico = df_materia_ex[df_materia_ex['PARALELO']>=100].reset_index()
#             paralel='Práctico'
#             for i in range(p_practico.shape[0]):
#                 datos=[]
#                 num_paralelo=p_practico['PARALELO'][i]
#                 num_registros=p_practico['NUMREGISTRADOS'][i]
#                 l_num_regis=f'Estudiantes Registrados: {num_registros}'
#                 datos.append(l_num_regis)
#                 bloque=p_practico['BLOQUE'][i]
#                 l_bloque=f'Bloque: {bloque}'
#                 datos.append(l_bloque)
#                 aula=p_practico['AULA'][i]
#                 l_aula=f'Aula: {aula}'
#                 datos.append(l_aula)
#                 hora1=str(p_practico['HORAINICIO'][i])[11:13]
#                 hora2=str(p_practico['HORAFIN'][i])[11:13]
#                 l_fecha= f'Hora del Exámen: {hora1} - {hora2} hrs'
#                 datos.append(l_fecha)
#                 df_materia_u.loc[i_df]=[selected_materia,fecha_texto,paralel,f'Paralelo {num_paralelo}',num_registros,bloque,aula,f'{hora1} - {hora2}','<br>'.join(datos)]
#                 i_df+=1
    
#     fig = px.treemap(df_materia_u,path=['NOMBRE','EXAMEN','TIPOPARALELO','BLOQUE','PARALELO','DATOS'],maxdepth=3,
#                      color_discrete_sequence=px.colors.qualitative.Pastel1)
#     fig.update_traces(marker=dict(cornerradius=5))
#     fig.update_layout(
#         bargap=0.1,
#         margin=dict(t=25, b=5, l=5, r=5),
#         template='plotly_dark', 
#         plot_bgcolor='rgb(255,255,255)',
#         paper_bgcolor='rgb(255,255,255)',
#         font=dict(
#             family="Droid Serif, monospace",
#             size=14,
#             color="black"))

#     return fig

# @app.callback(
#     Output('dropdown_campus_bloque_bar', 'value'),
#     Input('dropdown_campus_treemap', 'value'))
# def campus_bar_value(selected_campus):
#     return selected_campus

# @app.callback(
#     Output('dropdown_facultades_bloque_bar', 'options'),
#     Input('dropdown_campus_bloque_bar', 'value'))
# def set_facultad_options(selected_campus):
#     df_camp = df[df['CAMPUS']==selected_campus]
#     return [{'label': i, 'value': i} for i in df_camp['UNIDAD'].unique()]

# @app.callback(
#     Output('dropdown_facultades_bloque_bar', 'value'),
#    Input('dropdown_facultades_treemap', 'value'))
# def get_facultad_value(valor_prede):
#     return valor_prede

# @app.callback(
#     Output('dropdown_bloque_bar', 'options'),
#     [Input('dropdown_facultades_bloque_bar', 'value'),
#      Input('dropdown_campus_bloque_bar', 'value')])
# def set_bloque_options(selected_facultad,selected_campus):
#     df_bloque = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)]
#     return [{'label': i, 'value': i} for i in df_bloque['BLOQUE'].unique()]

# @app.callback(
#     Output('dropdown_bloque_bar', 'value'),
#    Input('dropdown_bloque_bar', 'options'))
# def get_bloque_value(v_prede):
#     return [k['value'] for k in v_prede][0]

# @app.callback(
#     Output('dropdown_examenes_bloque_bar', 'options'),
#     [Input('dropdown_facultades_bloque_bar', 'value'),
#      Input('dropdown_campus_bloque_bar', 'value'),
#      Input('dropdown_bloque_bar', 'value')])
# def set_bloque_options(selected_facultad,selected_campus,selected_bloque):
#     df_exa = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)&(df['BLOQUE']==selected_bloque)]
#     return [{'label': i, 'value': i} for i in df_exa['EXAMEN'].unique()]

# @app.callback(
#     Output('dropdown_examenes_bloque_bar', 'value'),
#    Input('dropdown_examenes_bloque_bar', 'options'))
# def get_examen_value(v_prede):
#     return [k['value'] for k in v_prede][0]

# @app.callback(
#     Output('dropdown_hora','options'),
#     [Input('dropdown_bloque_bar', 'value'),
#     Input('dropdown_campus_bloque_bar', 'value'),
#     Input('dropdown_facultades_bloque_bar', 'value'),
#     Input('dropdown_examenes_bloque_bar', 'value')] )
# def set_options_hour(selected_bloque,selected_campus,selected_facultades,selected_examen):
#     df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
#     df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA_INICIO'])
#     h=0
    
#     for materia in df_bloque_hist['NOMBRE'].unique():
#         materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
#         horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
#         horaei= int(horaistr[11])
#         if horaei == 0:
#             horaei= int(horaistr[12])         
#         else:
#             horaei= int(horaistr[11:13])
#         df_bloque_bar.loc[h]=[materia,horaei]
#         h+=1
#     df_hora=df_bloque_bar.HORA_INICIO.sort_values().reset_index()
#     return [{'label': i, 'value': i} for i in df_hora['HORA_INICIO'].unique()]

# @app.callback(
#     Output('dropdown_hora','value'),
#     Input('dropdown_hora','options'))
# def get_hour_value(v_prede):
#     return [k['value'] for k in v_prede][0]

# @app.callback(
#     Output('graph_bloque_bar', 'figure'),
#     [Input('dropdown_bloque_bar', 'value'),
#     Input('dropdown_campus_bloque_bar', 'value'),
#     Input('dropdown_facultades_bloque_bar', 'value'),
#     Input('dropdown_examenes_bloque_bar', 'value'),
#     Input('dropdown_hora','value')] )
# def update_figure(selected_bloque,selected_campus,selected_facultades,selected_examen,selected_hora_inicio):
#     df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
#     df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA','CANT_PARALELOS','REGISTRADOS','HORA_INICIO'])
#     h=0
#     for materia in df_bloque_hist['NOMBRE'].unique():
#         materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
#         cant_paralelos=len(materia_bloque['PARALELO'].unique())
#         cant_registrados=materia_bloque['PARALELO'].sum()
#         horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
#         horafstr= materia_bloque['HORAFIN'][0].strftime('%Y-%m-%d %H:%M:%S')
#         horaei= int(horaistr[11])
#         horaef=int(horafstr[11])
#         if horaei == 0:
#             horaei= int(horaistr[12])
#             if horaei <8:
#                 horaef= int(horafstr[12])
#             else:
#                 horaef= horafstr[11:13]          
#         else:
#             horaei= int(horaistr[11:13])
#             horaef= int(horafstr[11:13])
#         hora=f'({horaei} - {horaef})'
#         df_bloque_bar.loc[h]=[materia,hora,cant_paralelos,cant_registrados,horaei]
#         h+=1
#     df_utilizar_bar=df_bloque_bar[df_bloque_bar['HORA_INICIO']==selected_hora_inicio]
#     df_utilizar_bar.drop(['HORA_INICIO'], axis=1, inplace=True)
#     df_utilizar_bar.sort_values('MATERIA',inplace=True)

#     fig= px.bar(df_utilizar_bar,x='MATERIA',y='CANT_PARALELOS',barmode='group')
#     # tabla=dash_table.DataTable(df_utilizar_bar,columns=[{"name": i, "id": i} for i in df_utilizar_bar.columns])
#     return fig

# @app.callback(
#     Output('bloque_tabla', 'children'),
#     [Input('dropdown_bloque_bar', 'value'),
#     Input('dropdown_campus_bloque_bar', 'value'),
#     Input('dropdown_facultades_bloque_bar', 'value'),
#     Input('dropdown_examenes_bloque_bar', 'value'),
#     Input('dropdown_hora','value')] )
# def update_tabla(selected_bloque,selected_campus,selected_facultades,selected_examen,selected_hora_inicio):
#     df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
#     df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA','CANT_PARALELOS','REGISTRADOS','HORA_INICIO'])
#     h=0
#     for materia in df_bloque_hist['NOMBRE'].unique():
#         materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
#         cant_paralelos=len(materia_bloque['PARALELO'].unique())
#         cant_registrados=materia_bloque['PARALELO'].sum()
#         horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
#         horafstr= materia_bloque['HORAFIN'][0].strftime('%Y-%m-%d %H:%M:%S')
#         horaei= int(horaistr[11])
#         horaef=int(horafstr[11])
#         if horaei == 0:
#             horaei= int(horaistr[12])
#             if horaei <8:
#                 horaef= int(horafstr[12])
#             else:
#                 horaef= horafstr[11:13]          
#         else:
#             horaei= int(horaistr[11:13])
#             horaef= int(horafstr[11:13])
#         hora=f'({horaei} - {horaef})'
#         df_bloque_bar.loc[h]=[materia,hora,cant_paralelos,cant_registrados,horaei]
#         h+=1
#     df_utilizar_bar=df_bloque_bar[df_bloque_bar['HORA_INICIO']==selected_hora_inicio]
#     df_utilizar_bar.drop(['HORA_INICIO'], axis=1, inplace=True)
#     df_utilizar_bar.sort_values('MATERIA',inplace=True)
    
#     return html.Div([
#                 html.H4(f'Materias Activas a las {selected_hora_inicio} ',style={'textAlign':'center'}),
#                 dash_table.DataTable(
#                                     id='table_materias',
#                                     columns=[{'name':col, 'id':col}for col in df_utilizar_bar.columns],
#                                     data=df_utilizar_bar.to_dict('records'),  # the contents of the table
#                                     cell_selectable=True,  # para que no se me presente el hover
#                                     fill_width=False,
#                                     sort_action='native',
#                                     style_as_list_view=True,
#                                     style_header={
#                                         'backgroundColor': '#edf3f4',
#                                         'fontWeight': 'bold',
#                                         'textAlign': 'center'
#                                     },
#                                     style_cell={
#                                         'backgroundColor': '#edf3f4',
#                                         'textAlign': 'center',
#                                         'padding': '5px',
#                                         'textAlign': 'center'
#                                     },
#                                     style_data={'borderBottom': '1px solid #167ac6',
#                                                 'fontFamily': 'Quicksand',
#                                                 })],style={'margin':'2vw'})


# @app.callback(
#    Output('bars_facu','figure')
#     ,Input('select_facu','value'))
# def putvalue(value):
#     aa=df[df['UNIDAD']==value]
#     a=aa.groupby('BLOQUE').agg({'EXAMEN':'count'})
#     a.sort_values('EXAMEN', ascending=False, inplace=True)
#     fig=px.bar(a, x=a.index, y ='EXAMEN', color=a.index, orientation='v')
#     fig.update_xaxes(tickangle= 69) 
    
#     return fig

# @app.callback(
#     Output('boxplot', 'figure')
#     ,Output('scatterplot','figure')
#     ,Output('boxplot', 'style')
#     ,Output('scatterplot','style')
#     ,Input('select_facu2','value')
#     ,Input('checklist_figs','value')
    
# )
# def Mostrar_Ocultar_boxNscatter(value,checklist_value):
#     filtered_df= Ex_U[Ex_U['UNIDAD']==value].groupby('DOCENTE').agg({'AULA':'count'})
#     figbx=px.strip(filtered_df, y=filtered_df['AULA'], color=filtered_df.index, stripmode='group')
#     figbx.add_trace(go.Box(y=filtered_df['AULA'],name='figure', jitter=0.5, fillcolor='blue'))
#     figbx.update_yaxes(title_text='Cantidad de aulas')
#     figbx.update_layout(width=600)
#     figbx.update_traces(width=0.9)
    
#     figsct =px.scatter(x=None, y=filtered_df['AULA'], color=filtered_df.index, size=filtered_df['AULA']*0.005, labels={'y':'','x':''})
#     figsct.update_xaxes(type='category')
#     figsct.update_layout(autosize=False, width=600)
#     s_uno = {'display': 'inline-block'} if 'boxplot' in checklist_value else {'display': 'none'}
#     s_dos = {'display': 'inline-block'} if 'scatterplot' in checklist_value else {'display': 'none'}
#     return figbx,figsct, s_uno,s_dos

# @app.callback(
#     Output('tabs-content-graph','children')
#     ,Input('tabs-graph','value')
#     ,Input('select_bloque1','value')
#     ,Input('select_bloque2','value')
# )
# def tab_graph(value_tab,value_dropdown1,value_dropdown2):
    
#     if value_tab=='pregrado_label':
#         d=(Ex_U_es[Ex_U_es['BLOQUE']==value_dropdown1]).groupby(by=['DIA','AULA','HORAINICIO']).agg({'EXAMEN':'count'})
#         d.reset_index(level='HORAINICIO',inplace=True)
#         d.reset_index(level='AULA', inplace=True)
#         d.drop(columns='EXAMEN',inplace=True)
#         fig1= px.scatter(d,x=d.index,y='HORAINICIO', color='AULA')
        
#         return html.Div([
#             html.H3(f'BLOQUE: {value_dropdown1}', style={'marginTop':'2.5vh','marginLeft':'1vw'})
#             ,dcc.Graph(figure=fig1)])
        
#     elif value_tab=='grado_label':
#         d=(Ex_U_fds[Ex_U_fds['BLOQUE']==value_dropdown2]).groupby(by=['DIA','AULA','HORAINICIO']).agg({'EXAMEN':'count'})
#         d.reset_index(level='HORAINICIO',inplace=True)
#         d.reset_index(level='AULA', inplace=True)
#         d.drop(columns='EXAMEN',inplace=True)
#         fig2= px.scatter(d,x=d.index,y='HORAINICIO', color='AULA')
        
#         return html.Div([
#             html.H3(f'BLOQUE: {value_dropdown2}', style={'marginTop':'2.5vh','marginLeft':'1vw'})
#             ,dcc.Graph(figure=fig2)]) 
#       return html.Div([
#            dcc.Graph(figure=fig2)]) 
        