import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

import dash
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import datetime as dt

from app import app

#Gryffindor
df = pd.read_excel('Dashboard/pages/RptPlanifHorarioExam_20230120.xlsx')

for c in df.columns:
   if df[c].nunique() == 1:
       df.drop(c, axis="columns", inplace=True)

df.drop(columns="EMAIL", inplace=True)

df['HINICIO'] = df['HORAINICIO'].dt.hour.astype(object)
df['HFIN'] = df['HORAFIN'].dt.hour.astype(object)
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

faccolors=["#446038", "#11b0be", "#feda04", "#1b6cb3",
            "#59368a", '#dc2284', '#53ac33', "#7393a8", "#264067"]

#Slytherin
df_H_p=pd.read_csv('Dashboard/pages/df_Treemap_scatter.csv')
dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves','viernes']
clase_orden = ['Teórico','Práctico']
df_H_p.DIA = pd.Categorical(df_H_p['DIA'], dias_ordenados)
df_H_p.CLASE = pd.Categorical(df_H_p['CLASE'], clase_orden)
df_H_p.sort_values('DIA', inplace=True)
df_H_p.sort_values('CLASE', inplace=True)
cond=[df_H_p['COURSE']==1,df_H_p['COURSE']==2,df_H_p['COURSE']==3,df_H_p['COURSE']==4,df_H_p['COURSE']==5]
res=['COURSE 1','COURSE 2','COURSE 3','COURSE 4','COURSE 5']
df_H_p['COURSE'] = np.select(cond,res,default=df_H_p['COURSE'])
df_H_p['COURSE'] = pd.Categorical(df_H_p['COURSE'], res)
df_H_p.sort_values('COURSE', inplace=True)
h_inicial= dt.datetime(2023, 1, 1, 9, 0, 0)
h_final=dt.datetime(2023, 1, 1, 17, 1, 0)
mediahora=dt.timedelta(minutes=30)
time_30min =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(h_inicial,h_final,mediahora)]

df_mapa=pd.read_csv('Dashboard/pages/df_Mapa.csv')
faculta=list(df_mapa['UNIDAD'].unique())
faculta.append('Mapa Espol PAE')

df_H_p_t=pd.read_csv('Dashboard/pages/df_Treemap_scatter.csv')
df_facul = pd.DataFrame(df_H_p_t.UNIDAD.unique(),columns=['LEGENDA FACULTADES'])
h_inicial= dt.datetime(2023, 1, 1, 9, 0, 0)
h_final=dt.datetime(2023, 1, 1, 17, 1, 0)
mediahora=dt.timedelta(minutes=30)
time_30min =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(h_inicial,h_final,mediahora)]
colores_f = {
    'Facultad de Ciencias de la Vida':'rgb(213, 245, 227)',
    'Facultad de Ciencias Naturales y Matemáticas':'rgb(232, 218, 239)',
    'Facultad de Ingeniería en Electricidad y Computación':'rgb(214, 219, 223)',
    'Facultad de Ciencias Sociales y Humanísticas':'rgb(252, 243, 207)',
    'ESCUELA SUPERIOR POLITECNICA DEL LITORAL':'rgb(214,234,248)'
}
def posibles_horas(hi,hf):
    hi = pd.to_datetime(str(hi))
    hf=pd.to_datetime(str(hf))
    l_posibles_horas =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(hi,hf,dt.timedelta(minutes=30))]
    return l_posibles_horas
df_H_p_t['HORAS_POSIBLES'] = [ posibles_horas (hi,hf) for hi,hf in zip(df_H_p_t.HORAINICIO,df_H_p_t.HORAFIN)]

#Diseño de Grado
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("GRADO", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        html.Div([
            html.Div(children=[html.Label('Periodo'), 
                               dcc.Dropdown(['PAO I', 'PAO II', 'PAE'], 
                                            'PAE',
                                            id='periodo')],
                                            style={'flex':1,'padding':'1vw'}),
        html.Div(children=[html.Label('Año'),
                           dcc.Dropdown(['2022','2023'],
                                        '2023',
                                        id='año')],
                                        style={'flex':1,'padding':'1vw'}),
        html.Div(html.Button(id='search', n_clicks=0, children='Search', style={'flex':1, 'height':'5vh', 'width':'5vw', 'borderRadius':'0.3vw','backgroundColor':'Transparent','borderWidth':'0.15vw','borderColor':'grey'}),
                 style={'paddingTop':'5.4vh'})
        ],
        style={'display':'flex','flexDirection':'row'}),
        html.Div(html.H1('Horarios'),style={'paddingLeft':'1vw','marginTop':'2vh'}),
        html.Div(id='horario'),
        html.Div(html.H1('Examenes'),style={'paddingLeft':'1vw','marginTop':'2vh'}),
        html.Div(id='examenes'),

    ])
])

@app.callback(
   Output('horario','children'),
   Output('examenes','children'),
   Input('search','n_clicks'),
   State('periodo','value'),
   State('año','value')
)
def filter_content(filtrar,periodo,año):
   if periodo == 'PAE' and año == '2023':
      return html.Div([dbc.Row([ html.H2('HORARIO PAE',style={'margin-left':'2vw'})]),
        html.Div([
            html.P('Seleccione una Facultad :'),
            dcc.Dropdown(
                df_H_p.UNIDAD.unique(),
                'Facultad de Ciencias de la Vida',
                id='dropdown_facultades',),
            html.P('Materias Disponibles :',style={'margin-top':'2vw'}), 
            dcc.Dropdown([],id='dropdown_materias_facul')],style={"margin":"2vw"}),
        html.Div([
            html.Div([
                dcc.Graph(id='graph_treemap')])
            ],style={"margin":"2vw","color":"black"}),
        html.Div([
            html.Button('HORARIO DINÁMICO', id='show_div')],style={"display": "flex","justify-content": "center","align-items": "center"}),
        html.Div(id='body_div',style={'margin':'2vw'}),
        html.Div([
            html.H2('MAPA DE UBICACIÓN DE AULAS'),
            dcc.Dropdown(faculta,'Mapa Espol PAE',id='facul_drop',style={'margin':'1vw 0 1vw 0'}),
            dcc.Graph(id='Facultad'),
        html.Div([
            html.Div([
                html.H2('TABLA DE MATERIAS ACTIVAS')],style={'margin-top':'4vw'}),
        html.Div([
            html.Div([
                html.Div([
                html.P('Seleccione una Facultad :'),
                dcc.Dropdown(
                    list(df_H_p_t.UNIDAD.unique())+['Todas las Facultades'],
                    'Facultad de Ciencias de la Vida',
                    id='dropdownfacultades',style={'width':'45vw'})],style={'margin':'2vw'}),
                #html.P('Materias Disponibles :')] 
                #dcc.Dropdown([],id='dropdown_materias_facul')]
                html.Div([
                html.P('Seleccione un Dia :'),
                dcc.Dropdown(['lunes','martes','miércoles','jueves'],'lunes',id='dropdown_dia',style={'width':'18vw',})],style={'margin':'2vw'}),
                html.Div([
                html.P('Seleccione una Hora :'),
                dcc.Dropdown(time_30min+['Todo el día'],'09:00:00',id='dropdown_hora',style={'width':'18vw'})],style={'margin':'2vw'})
                ],className='selector',style={'display':'flex','justify-content':'center','align-items':'center','width':'60vw',"margin":"2vw"}),
                ],id='header_search',style={'display':'flex','justify-content':'center','align-items':'center'}),
        html.Div([
            html.Div([],className="container_table",id='container_table',style={'margin-right':'5vw','margin-left':'5vw'})
            ],className='container_table',style={"display": "flex","justify-content": "center","align-items": "center",'margin-top':'2vw'}),
            ],id="main_container_table", style={"display": "flex", "flex-direction": "column"})
            ],id ='main_container_mapa', style={"display": "flex", "flex-direction": "column",'margin':'2vw'}), #Arriba | Derecha | Abajo | Izquierda
        html.Div(id='container_flujo',style={'margin':'2vw'}),
        html.Div([
            html.Button('INSIGHTS', id='show_insights'),],style={"display": "flex","justify-content": "center","align-items": "center"}),
        html.Div(id='Insights_div',style={'margin':'2vw'}),
        html.Div(id='container_insight',style={'textAlign':'justify','margin':'2vw'})]), html.H5('No hay datos de este periodo',style={'margin':'2vw'})
   
   elif periodo == 'PAO II' and año == '2022':
      return  html.H5('No hay datos de este periodo',style={'margin':'2vw'}), html.Div([
         html.Div([html.H2('HORARIO DE EXÁMENES - II PAO 2022'),
                html.H3('Detalles de las materias',style={'margin-top':'4vw'}),
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
                ]),


                html.Div([
                html.Div([
                    html.H3('Cantidad de examenes tomados por cada bloque',style={'margin-top':'4vw'})
                    , html.P('Seleccione una facultad:')
                    , dcc.Dropdown(
                        df.UNIDAD.unique(), 'Faculta de Ciencias Sociales y Humanísticas', id='select_facu')],style={'margin-top':'2vw'}
                    )
                , html.Div([
                    dcc.Graph(id='bars_facu')
                ])
                ]),

            html.Div([
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
            #html.Div([
                    html.H3('Distribución de exámenes',style={'margin-top':'4vw'}),
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
                dcc.Graph(id='graph_timeline')],style={'margin':'2vw'})
                , html.Div([ 
                    html.H3('Distribución de aulas por horario')
                    , dcc.Tabs(id="tabs-graph", 
                               children=[
                         dcc.Tab(label='Pregrado', value='pregrado_label', children=[
                             html.P('Seleccione Bloque:', style={'marginTop':'3vh'}) 
                            ,dcc.Dropdown(Ex_U_es.BLOQUE.unique(),id='select_bloque1') ])
                        , dcc.Tab(label='Grado', value='grado_label', children=[
                            html.P('Seleccione Bloque:', style={'marginTop':'3vh'}) 
                            ,dcc.Dropdown(Ex_U_fds.BLOQUE.unique(),id='select_bloque2') ])
                        ])
                    , html.Div(id='tabs-content-graph')]),html.Br()
            , html.Div([
                    html.H3('Distribución de docentes presentes en aulas por facultad',style={'marginTop':'5vh'})
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

                    ])], style={"display": "flex", "flex-direction": "column",'margin':'4vw'})
   else:
       return html.H5('No hay datos de este periodo',style={'margin':'2vw'}),html.H5('No hay datos de este periodo',style={'margin':'2vw'})
          
#Gryffindor callbacks
@app.callback(Output('graph_timeline', 'figure'),
    [Input('dropdown_examen', 'value'),
    Input('dropdown_bloques', 'value')])   
def update_figure(examen_selected,bloque_selected):
    df_timeline = campusdf[(campusdf['BLOQUE'] == bloque_selected) & (campusdf['EXAMEN'] == examen_selected)]
    fig_timeline = px.timeline(df_timeline, x_start = "HORAINICIO", x_end = "HORAFIN", y = "AULA",
                        color = "UNIDAD", title="Distribución de aulas de éxamenes por bloque y por intervalos de tiempo.",
                        hover_name = "NOMBRE")
    return fig_timeline

@app.callback(
    Output('dropdown_facultades_treemap', 'options'),
    Input('dropdown_campus_treemap', 'value'))
def set_facultad_options(selected_campus):
    df_camp = df[df['CAMPUS']==selected_campus]
    return [{'label': i, 'value': i} for i in df_camp['UNIDAD'].unique()]

@app.callback(
    Output('dropdown_facultades_treemap', 'value'),
   Input('dropdown_facultades_treemap', 'options'))
def get_facultad_value(valor_prede):
    return [k['value'] for k in valor_prede][0]

@app.callback(
    Output('dropdown_materias_disp_treemap', 'options'),
    [Input('dropdown_facultades_treemap', 'value'),
    Input('dropdown_campus_treemap', 'value')] )
def set_materias_options(selected_facultad,selected_campus):
    df_uni = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)]
    return [{'label': i, 'value': i} for i in df_uni['NOMBRE'].unique()]

@app.callback(
    Output('dropdown_materias_disp_treemap', 'value'),
   Input('dropdown_materias_disp_treemap', 'options'))
def get_materia_value(v_prede):
    return [k['value'] for k in v_prede][0]

@app.callback(Output('graph_treemap_mat', 'figure'),
    [Input('dropdown_campus_treemap', 'value'),
    Input('dropdown_facultades_treemap', 'value'),
    Input('dropdown_materias_disp_treemap', 'value')])
def update_figure(selected_campus,selected_facultad,selected_materia):
    df_materia_final=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)&(df['NOMBRE']==selected_materia)]
    examenes = df_materia_final['EXAMEN'].unique()
    i_df=0
    df_materia_u = pd.DataFrame(columns=['NOMBRE','EXAMEN','TIPOPARALELO','PARALELO','NUMREGISTRADOS','BLOQUE','AULA','HORA','DATOS'])
    for examen in examenes:
        paralel = 'Teórico'
        df_materia_ex = df_materia_final[df_materia_final['EXAMEN']==examen].reset_index()
        fecha = str(df_materia_ex['FECHA'][0])[:11].replace('-','/')
        dia = df_materia_ex['DIA'][0]
        fecha_texto = f'Examen {examen} - {fecha} ({dia})'
        print(fecha_texto)
        p_teo = df_materia_ex[df_materia_ex['PARALELO']<100].reset_index()
        for i in range(p_teo.shape[0]):
            datos=[]
            num_paralelo=p_teo['PARALELO'][i]
            num_registros=p_teo['NUMREGISTRADOS'][i]
            l_num_regis=f'Estudiantes Registrados: {num_registros}'
            datos.append(l_num_regis)
            aula=p_teo['AULA'][i]
            bloque=p_teo['BLOQUE'][i]
            l_bloque=f'Bloque: {bloque}'
            datos.append(l_bloque)
            l_aula=f'Aula: {aula}'
            datos.append(l_aula)
            hora1=str(p_teo['HORAINICIO'][i])[11:13]
            hora2=str(p_teo['HORAFIN'][i])[11:13]
            l_fecha= f'Hora del Exámen: {hora1} - {hora2} hrs'
            datos.append(l_fecha)
            df_materia_u.loc[i_df]=[selected_materia,fecha_texto,paralel,f'Paralelo {num_paralelo}',num_registros,bloque,aula,f'{hora1} - {hora2}','<br>'.join(datos)]
            i_df+=1 
        if df_materia_ex[df_materia_ex['PARALELO']>=100].shape[0] >0:
            p_practico = df_materia_ex[df_materia_ex['PARALELO']>=100].reset_index()
            paralel='Práctico'
            for i in range(p_practico.shape[0]):
                datos=[]
                num_paralelo=p_practico['PARALELO'][i]
                num_registros=p_practico['NUMREGISTRADOS'][i]
                l_num_regis=f'Estudiantes Registrados: {num_registros}'
                datos.append(l_num_regis)
                bloque=p_practico['BLOQUE'][i]
                l_bloque=f'Bloque: {bloque}'
                datos.append(l_bloque)
                aula=p_practico['AULA'][i]
                l_aula=f'Aula: {aula}'
                datos.append(l_aula)
                hora1=str(p_practico['HORAINICIO'][i])[11:13]
                hora2=str(p_practico['HORAFIN'][i])[11:13]
                l_fecha= f'Hora del Exámen: {hora1} - {hora2} hrs'
                datos.append(l_fecha)
                df_materia_u.loc[i_df]=[selected_materia,fecha_texto,paralel,f'Paralelo {num_paralelo}',num_registros,bloque,aula,f'{hora1} - {hora2}','<br>'.join(datos)]
                i_df+=1
    
    fig = px.treemap(df_materia_u,path=['NOMBRE','EXAMEN','TIPOPARALELO','BLOQUE','PARALELO','DATOS'],maxdepth=3,
                     color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_layout(
        bargap=0.1,
        margin=dict(t=25, b=5, l=5, r=5),
        template='plotly_dark', 
        plot_bgcolor='rgb(255,255,255)',
        paper_bgcolor='rgb(255,255,255)',
        font=dict(
            family="Droid Serif, monospace",
            size=14,
            color="black"))

    return fig

@app.callback(
    Output('dropdown_campus_bloque_bar', 'value'),
    Input('dropdown_campus_treemap', 'value'))
def campus_bar_value(selected_campus):
    return selected_campus

@app.callback(
    Output('dropdown_facultades_bloque_bar', 'options'),
    Input('dropdown_campus_bloque_bar', 'value'))
def set_facultad_options(selected_campus):
    df_camp = df[df['CAMPUS']==selected_campus]
    return [{'label': i, 'value': i} for i in df_camp['UNIDAD'].unique()]

@app.callback(
    Output('dropdown_facultades_bloque_bar', 'value'),
   Input('dropdown_facultades_treemap', 'value'))
def get_facultad_value(valor_prede):
    return valor_prede

@app.callback(
    Output('dropdown_bloque_bar', 'options'),
    [Input('dropdown_facultades_bloque_bar', 'value'),
     Input('dropdown_campus_bloque_bar', 'value')])
def set_bloque_options(selected_facultad,selected_campus):
    df_bloque = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)]
    return [{'label': i, 'value': i} for i in df_bloque['BLOQUE'].unique()]

@app.callback(
    Output('dropdown_bloque_bar', 'value'),
   Input('dropdown_bloque_bar', 'options'))
def get_bloque_value(v_prede):
    return [k['value'] for k in v_prede][0]

@app.callback(
    Output('dropdown_examenes_bloque_bar', 'options'),
    [Input('dropdown_facultades_bloque_bar', 'value'),
     Input('dropdown_campus_bloque_bar', 'value'),
     Input('dropdown_bloque_bar', 'value')])
def set_bloque_options(selected_facultad,selected_campus,selected_bloque):
    df_exa = df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultad)&(df['BLOQUE']==selected_bloque)]
    return [{'label': i, 'value': i} for i in df_exa['EXAMEN'].unique()]

@app.callback(
    Output('dropdown_examenes_bloque_bar', 'value'),
   Input('dropdown_examenes_bloque_bar', 'options'))
def get_examen_value(v_prede):
    return [k['value'] for k in v_prede][0]

@app.callback(
    Output('dropdown_hora','options'),
    [Input('dropdown_bloque_bar', 'value'),
    Input('dropdown_campus_bloque_bar', 'value'),
    Input('dropdown_facultades_bloque_bar', 'value'),
    Input('dropdown_examenes_bloque_bar', 'value')] )
def set_options_hour(selected_bloque,selected_campus,selected_facultades,selected_examen):
    df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
    df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA_INICIO'])
    h=0
    
    for materia in df_bloque_hist['NOMBRE'].unique():
        materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
        horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
        horaei= int(horaistr[11])
        if horaei == 0:
            horaei= int(horaistr[12])         
        else:
            horaei= int(horaistr[11:13])
        df_bloque_bar.loc[h]=[materia,horaei]
        h+=1
    df_hora=df_bloque_bar.HORA_INICIO.sort_values().reset_index()
    return [{'label': i, 'value': i} for i in df_hora['HORA_INICIO'].unique()]

@app.callback(
    Output('dropdown_hora','value'),
    Input('dropdown_hora','options'))
def get_hour_value(v_prede):
    return [k['value'] for k in v_prede][0]

@app.callback(
    Output('graph_bloque_bar', 'figure'),
    [Input('dropdown_bloque_bar', 'value'),
    Input('dropdown_campus_bloque_bar', 'value'),
    Input('dropdown_facultades_bloque_bar', 'value'),
    Input('dropdown_examenes_bloque_bar', 'value'),
    Input('dropdown_hora','value')] )
def update_figure(selected_bloque,selected_campus,selected_facultades,selected_examen,selected_hora_inicio):
    df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
    df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA','CANT_PARALELOS','REGISTRADOS','HORA_INICIO'])
    h=0
    for materia in df_bloque_hist['NOMBRE'].unique():
        materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
        cant_paralelos=len(materia_bloque['PARALELO'].unique())
        cant_registrados=materia_bloque['PARALELO'].sum()
        horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
        horafstr= materia_bloque['HORAFIN'][0].strftime('%Y-%m-%d %H:%M:%S')
        horaei= int(horaistr[11])
        horaef=int(horafstr[11])
        if horaei == 0:
            horaei= int(horaistr[12])
            if horaei <8:
                horaef= int(horafstr[12])
            else:
                horaef= horafstr[11:13]          
        else:
            horaei= int(horaistr[11:13])
            horaef= int(horafstr[11:13])
        hora=f'({horaei} - {horaef})'
        df_bloque_bar.loc[h]=[materia,hora,cant_paralelos,cant_registrados,horaei]
        h+=1
    df_utilizar_bar=df_bloque_bar[df_bloque_bar['HORA_INICIO']==selected_hora_inicio]
    df_utilizar_bar.drop(['HORA_INICIO'], axis=1, inplace=True)
    df_utilizar_bar.sort_values('MATERIA',inplace=True)

    fig= px.bar(df_utilizar_bar,x='MATERIA',y='CANT_PARALELOS',barmode='group')
    # tabla=dash_table.DataTable(df_utilizar_bar,columns=[{"name": i, "id": i} for i in df_utilizar_bar.columns])
    return fig

@app.callback(
    Output('bloque_tabla', 'children'),
    [Input('dropdown_bloque_bar', 'value'),
    Input('dropdown_campus_bloque_bar', 'value'),
    Input('dropdown_facultades_bloque_bar', 'value'),
    Input('dropdown_examenes_bloque_bar', 'value'),
    Input('dropdown_hora','value')] )
def update_tabla(selected_bloque,selected_campus,selected_facultades,selected_examen,selected_hora_inicio):
    df_bloque_hist=df[(df['CAMPUS']==selected_campus)&(df['UNIDAD']==selected_facultades)&(df['BLOQUE']==selected_bloque)&(df['EXAMEN']==selected_examen)].reset_index()
    df_bloque_bar=pd.DataFrame(columns=['MATERIA','HORA','CANT_PARALELOS','REGISTRADOS','HORA_INICIO'])
    h=0
    for materia in df_bloque_hist['NOMBRE'].unique():
        materia_bloque=df_bloque_hist[(df_bloque_hist['NOMBRE']==materia)&(df_bloque_hist['PARALELO']<100)].reset_index()
        cant_paralelos=len(materia_bloque['PARALELO'].unique())
        cant_registrados=materia_bloque['PARALELO'].sum()
        horaistr= materia_bloque['HORAINICIO'][0].strftime('%Y-%m-%d %H:%M:%S')
        horafstr= materia_bloque['HORAFIN'][0].strftime('%Y-%m-%d %H:%M:%S')
        horaei= int(horaistr[11])
        horaef=int(horafstr[11])
        if horaei == 0:
            horaei= int(horaistr[12])
            if horaei <8:
                horaef= int(horafstr[12])
            else:
                horaef= horafstr[11:13]          
        else:
            horaei= int(horaistr[11:13])
            horaef= int(horafstr[11:13])
        hora=f'({horaei} - {horaef})'
        df_bloque_bar.loc[h]=[materia,hora,cant_paralelos,cant_registrados,horaei]
        h+=1
    df_utilizar_bar=df_bloque_bar[df_bloque_bar['HORA_INICIO']==selected_hora_inicio]
    df_utilizar_bar.drop(['HORA_INICIO'], axis=1, inplace=True)
    df_utilizar_bar.sort_values('MATERIA',inplace=True)
    
    return html.Div([
                html.H4(f'Materias Activas a las {selected_hora_inicio} ',style={'textAlign':'center'}),
                dash_table.DataTable(
                                    id='table_materias',
                                    columns=[{'name':col, 'id':col}for col in df_utilizar_bar.columns],
                                    data=df_utilizar_bar.to_dict('records'),  # the contents of the table
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
                                                'fontFamily': 'Quicksand',
                                                })],style={'margin':'2vw'})
    
    
@app.callback(
   Output('bars_facu','figure')
    ,Input('select_facu','value'))
def putvalue(value):
    aa=df[df['UNIDAD']==value]
    a=aa.groupby('BLOQUE').agg({'EXAMEN':'count'})
    a.sort_values('EXAMEN', ascending=False, inplace=True)
    fig=px.bar(a, x=a.index, y ='EXAMEN', color=a.index, orientation='v')
    fig.update_xaxes(tickangle= 69) 
    
    return fig

@app.callback(
    Output('boxplot', 'figure')
    ,Output('scatterplot','figure')
    ,Output('boxplot', 'style')
    ,Output('scatterplot','style')
    ,Input('select_facu2','value')
    ,Input('checklist_figs','value')
    
)
def Mostrar_Ocultar_boxNscatter(value,checklist_value):
    filtered_df= Ex_U[Ex_U['UNIDAD']==value].groupby('DOCENTE').agg({'AULA':'count'})
    figbx=px.strip(filtered_df, y=filtered_df['AULA'], color=filtered_df.index, stripmode='group')
    figbx.add_trace(go.Box(y=filtered_df['AULA'],name='figure', jitter=0.5, fillcolor='blue'))
    figbx.update_yaxes(title_text='Cantidad de aulas')
    figbx.update_layout(width=600)
    figbx.update_traces(width=0.9)
    
    figsct =px.scatter(x=None, y=filtered_df['AULA'], color=filtered_df.index, size=filtered_df['AULA']*0.005, labels={'y':'','x':''})
    figsct.update_xaxes(type='category')
    figsct.update_layout(autosize=False, width=600)
    s_uno = {'display': 'inline-block'} if 'boxplot' in checklist_value else {'display': 'none'}
    s_dos = {'display': 'inline-block'} if 'scatterplot' in checklist_value else {'display': 'none'}
    return figbx,figsct, s_uno,s_dos

@app.callback(
    Output('tabs-content-graph','children')
    ,Input('tabs-graph','value')
    ,Input('select_bloque1','value')
    ,Input('select_bloque2','value')
)
def tab_graph(value_tab,value_dropdown1,value_dropdown2):
    
    if value_tab=='pregrado_label':
        d=(Ex_U_es[Ex_U_es['BLOQUE']==value_dropdown1]).groupby(by=['DIA','AULA','HORAINICIO']).agg({'EXAMEN':'count'})
        d.reset_index(level='HORAINICIO',inplace=True)
        d.reset_index(level='AULA', inplace=True)
        d.drop(columns='EXAMEN',inplace=True)
        fig1= px.scatter(d,x=d.index,y='HORAINICIO', color='AULA')
        
        return html.Div([
            html.H3(f'BLOQUE: {value_dropdown1}', style={'marginTop':'2.5vh','marginLeft':'1vw'})
            ,dcc.Graph(figure=fig1)])
        
    elif value_tab=='grado_label':
        d=(Ex_U_fds[Ex_U_fds['BLOQUE']==value_dropdown2]).groupby(by=['DIA','AULA','HORAINICIO']).agg({'EXAMEN':'count'})
        d.reset_index(level='HORAINICIO',inplace=True)
        d.reset_index(level='AULA', inplace=True)
        d.drop(columns='EXAMEN',inplace=True)
        fig2= px.scatter(d,x=d.index,y='HORAINICIO', color='AULA')
        
        return html.Div([
            html.H3(f'BLOQUE: {value_dropdown2}', style={'marginTop':'2.5vh','marginLeft':'1vw'})
            ,dcc.Graph(figure=fig2)]) 
    

#Slytherin callbacks
@app.callback(
    Output('dropdown_materias_facul', 'options'),
    Input('dropdown_facultades', 'value'))
def set_cities_options(selected_facultad):
    dff = df_H_p[df_H_p['UNIDAD']==selected_facultad]
    return [{'label': i, 'value': i} for i in dff['NOMBRE'].unique()]

@app.callback(
    Output('dropdown_materias_facul', 'value'),
    Input('dropdown_materias_facul', 'options'))
def get_country_value(v_prede):
    return [k['value'] for k in v_prede][0]

@app.callback(Output('graph_treemap', 'figure'),
    [Input('dropdown_facultades','value')],
    [Input('dropdown_materias_facul', 'value')])
def update_figure(selected_facultad,selected_materia):

    def contruir_condi(n_course,n_clase):
        return (df_H_p['COURSE']== df_H_p.COURSE.unique()[n_course] ) & (df_H_p['CLASE']==df_H_p.CLASE.unique()[n_clase])
    #5 CURSOS Y 2 CLASES [Teórico y Práctico]
    cond=[contruir_condi(0,0),contruir_condi(1,0),contruir_condi(2,0),contruir_condi(3,0),contruir_condi(4,0),contruir_condi(0,1),contruir_condi(1,1),contruir_condi(2,1),contruir_condi(3,1),contruir_condi(4,1)]
    res=['A','B','C','D','E','F','G','H','I','J']
    df_H_p['COLORS'] = np.select(cond,res)
    df_H_p['TEXTO1'] = [f'<br>Paralelo: {paralelo}     Aula: {aula} 'for paralelo,aula in zip(df_H_p['PARALELO'],df_H_p['AULA'])]
    df_H_p['TEXTO2'] = [f'<br>Hora Entrada: <br> {hi} <br>Hora Salida: <br> {hf}' for hi,hf in zip(df_H_p['HORAINICIO'],df_H_p['HORAFIN'])]  #Hora de entrada y salida
    dff = df_H_p[df_H_p['UNIDAD']==selected_facultad]
    dff = dff[dff['NOMBRE']==selected_materia]
    fig = px.treemap(dff, path=['NOMBRE', 'COURSE','CLASE','DIA','TEXTO1','TEXTO2'],color='COLORS',maxdepth=4,
                    color_discrete_sequence=px.colors.qualitative.Pastel1,color_discrete_map={'A':'rgb(141,211,199)','B':'rgb(190,186,218)','C':'rgb(251,128,114)','D':'rgb(128,177,211)','F':'rgb(253,180,98)','E':'rgb(179,222,105)','G':'rgb(252,205,229)','H':'rgb(217,217,217)','I':'rgb(188,128,189)','J':'rgb(255,237,111)'})
    #diseño
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_layout(
        bargap=0.1,
        margin=dict(t=25, b=5, l=5, r=5),
        template='plotly_dark', 
        plot_bgcolor='rgb(255,255,255)',
        paper_bgcolor='rgb(255,255,255)',
        font=dict(
            family="Droid Serif, monospace",
            size=14,
            color="black"))
    return fig
def onlyteoric(df):
    st=list(df_H_p.NOMBRE[df_H_p.TIPOMATERIA == 'teórica'].unique())
    return st #solo teórico parte teórica
st=onlyteoric(df_H_p)
@app.callback(
    Output('body_div', 'children'),
    [Input('show_div', 'n_clicks')],
    [Input('dropdown_facultades','value')],
    [Input('dropdown_materias_facul', 'value')])
def update_output(n_clicks,selected_facultad,selected_materia):
    dff = df_H_p[df_H_p['UNIDAD']==selected_facultad]
    dff = dff[dff['NOMBRE']==selected_materia]
    if n_clicks is None:     # hasta que de click
        raise PreventUpdate
    else:
        if selected_materia in st:  # que solo me imprima un gráfico que pertenece a la parte teórica
            return html.Div([
            html.Div([
            html.P("Seleccione un Curso: "),
            dcc.RadioItems(dff.COURSE.unique(),id='radioitems_course')],id='selector',style={'display':'flex','flex-direction':'column','justify-content':'center','align-items':'center'}),
            html.Div([
                html.Div([
                dcc.Graph(id='graph_horario_teo',style={"width":"60vw"}),]
                ,style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center"})
            ],id='container_graphs',style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center"})
            ],id='body_div',style={'display':'flex','flex-direction':'column'})
        else:
            return html.Div([
            html.Div([
            html.P("Seleccione un Curso: "),
            dcc.RadioItems(dff.COURSE.unique(),id='radioitems_course')],id='selector',style={'display':'flex','flex-direction':'column','justify-content':'center','align-items':'center'}),
            html.Div([
                html.Div([
                dcc.Graph(id='graph_horario_teo',style={"width":"40vw"}),
                dcc.Graph(id='graph_horario_pra',style={"width":"40vw"})],style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center",'margin-top':'2vw'}),
            ],id='container_graphs',style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center"}),
            ],id='body_div',style={'display':'flex','flex-direction':'column'})
#TOMAR PREDETERMINADO 
@app.callback(
    Output('radioitems_course', 'value'),
    Input('radioitems_course', 'options'))
def get_country_value(v_prede):
    return v_prede[0]

@app.callback(
    Output('graph_horario_teo', 'figure'),
    [Input('dropdown_facultades','value')],
    [Input('dropdown_materias_facul', 'value')],
    [Input('radioitems_course', 'value')])
def update_figure(selected_facultad,selected_materia,selected_course):
    dff = df_H_p[df_H_p['UNIDAD']==selected_facultad]
    dff = dff[dff['NOMBRE']==selected_materia]
    dff = dff[dff['COURSE']==selected_course]
    dff = dff[dff.CLASE=='Teórico']
    if selected_course is None:
        raise PreventUpdate
    df_horarios = pd.DataFrame(columns=['HORARIOS','INDICADOR','SIZE','PARALELO','DIA','CLASE','AULA'])
    def armar_dataset(colum):
        return list(dff[colum]) + list(dff[colum])
    df_horarios.HORARIOS = list(dff.HORAINICIO ) + list(dff.HORAFIN ) 
    df_horarios.INDICADOR = ['INGRESO']* dff.shape[0]+ ['SALIDA']* dff.shape[0]
    df_horarios['SIZE'] =[10]*df_horarios.shape[0]
    columns = list(df_horarios.columns)
    for x in [0]*3:
        columns.pop(x)
    for colum in columns:
        df_horarios[colum] = armar_dataset(colum)
    #ORDENAR LAS FECHAS 
    dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves','viernes']
    df_horarios.DIA = pd.Categorical(df_horarios['DIA'], dias_ordenados)
    #df_horarios.HORARIOS = pd.to_datetime(df_horarios.HORARIOS ,format="%X")
    df_horarios.sort_values('DIA',inplace=True)
    #df_horarios.HORARIOS=[dt.datetime.strptime(str(t),'%Y-%m-%d %H:%M:%S').time() for  t in df_horarios['HORARIOS']]
    #df_horarios.sort_values(['HORARIOS'],inplace=True)


    fig = px.scatter(df_horarios, y="DIA", x="HORARIOS",color='INDICADOR',symbol='INDICADOR',facet_row='PARALELO',size='SIZE',hover_data=['PARALELO','AULA','CLASE'])
    fig.update_traces(showlegend=True)
    fig.update_layout(
            title={
            'text' :'Teórico',
            'x':0.5,
            'xanchor': 'center'
        })
    fig.update_yaxes(categoryarray=['lunes','martes','miércoles','jueves','viernes'])
    fig.update_xaxes(categoryarray=time_30min)
    fig.update_xaxes(tickangle=90)
    return fig

@app.callback(
    Output('graph_horario_pra', 'figure'),
    [Input('dropdown_facultades','value')],
    [Input('dropdown_materias_facul', 'value')],
    [Input('radioitems_course', 'value')])
def update_figure(selected_facultad,selected_materia,selected_course):
    dff = df_H_p[df_H_p['UNIDAD']==selected_facultad]
    dff = dff[dff['NOMBRE']==selected_materia]
    dff = dff[dff['COURSE']==selected_course]
    dff = dff[dff.CLASE=='Práctico']
    if selected_course is None:
        raise PreventUpdate
    df_horarios = pd.DataFrame(columns=['HORARIOS','INDICADOR','SIZE','PARALELO','DIA','CLASE','AULA'])
    def armar_dataset(colum):
        return list(dff[colum]) + list(dff[colum])
    df_horarios.HORARIOS = list(dff.HORAINICIO ) + list(dff.HORAFIN ) 
    df_horarios.INDICADOR = ['INGRESO']* dff.shape[0]+ ['SALIDA']* dff.shape[0]
    df_horarios['SIZE'] =[10]*df_horarios.shape[0]
    columns = list(df_horarios.columns)
    for x in [0]*3:
        columns.pop(x)
    for colum in columns:
        df_horarios[colum] = armar_dataset(colum)
    #ORDENAR LAS FECHAS 
    dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves','viernes']
    df_horarios.DIA = pd.Categorical(df_horarios['DIA'], dias_ordenados)
    #df_horarios.HORARIOS = pd.to_datetime(df_horarios.HORARIOS ,format="%X")
    df_horarios.sort_values('DIA',inplace=True)
    #df_horarios.HORARIOS=[str(t).split(" ")[1] for  t in df_horarios['HORARIOS']]
    #df_horarios.sort_values(['HORARIOS'],inplace=True)


    if selected_materia in ['PRINCIPIOS DE ELECTRÓNICA','SISTEMAS DIGITALES I']:
        height=900
    elif selected_materia == 'TÉCNICAS DIETÉTICAS':
        height=600
    else:
        height=None

    fig = px.scatter(df_horarios, y="DIA", x="HORARIOS",color='INDICADOR',symbol='INDICADOR',facet_row='PARALELO',size='SIZE',hover_data=['PARALELO','AULA'],height=height)
    fig.update_layout(
            title={
            'text' : 'Práctico',
            'x':0.5,
            'xanchor': 'center'
        })
    fig.update_yaxes(categoryarray=['lunes','martes','miércoles','jueves','viernes'])
    fig.update_xaxes(categoryarray=time_30min)
    fig.update_xaxes(tickangle=90)
    return fig


def mapaEspol(df,lat,lon,zo):
    fig1 = px.scatter_mapbox(df, lat="lat2", lon="lon2", hover_data=["BLOQUE", "CAPACIDAD", 'CLASE'],
                            zoom=zo, height=600,color='NOMBRE',size='CAPACIDAD')
    fig1.update_layout(mapbox_style="open-street-map", mapbox=dict(
            center=dict(
                lat=lat,
                lon=lon
            ),))
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  
    return fig1

@app.callback(
    Output('Facultad','figure'),
    Input('facul_drop','value')
)
def mapa(value):
    if value=='Mapa Espol PAE':
        fig1=mapaEspol(df_mapa,-2.14730,-79.9630,15)          
    elif value=='Facultad de Ingeniería en Electricidad y Computación':
        df_facul=df_mapa[df_mapa['UNIDAD']==value]
        fig1 = mapaEspol(df_facul,-2.14466,-79.96772,17.5)       
    elif  value=='Facultad de Ciencias Sociales y Humanísticas':
        df_facul=df_mapa[df_mapa['UNIDAD']==value]
        fig1 = mapaEspol(df_facul,-2.14873,-79.96782,17)    
    elif value=='Facultad de Ciencias Naturales y Matemáticas':
        df_facul=df_mapa[df_mapa['UNIDAD']==value]
        fig1 = mapaEspol(df_facul,-2.14662,-79.96666,18.3)  
    elif value=='Facultad de Ciencias de la Vida':
        df_facul=df_mapa[df_mapa['UNIDAD']==value]
        fig1 = mapaEspol(df_facul,-2.15122,-79.95424,17)
    elif value=='ESCUELA SUPERIOR POLITECNICA DEL LITORAL':
        df_facul=df_mapa[df_mapa['UNIDAD']==value]
        fig1 = mapaEspol(df_facul,-2.14589,-79.96530,17)
    return fig1

@app.callback(
    Output('container_table','children'),
    [Input('dropdownfacultades', 'value')],
    [Input('dropdown_hora','value')],
    [Input('dropdown_dia','value')])
def create_table(selected_facultad,selected_hora,selected_dia):
    if selected_facultad == 'Todas las Facultades':
        if selected_hora!='Todo el día':
            dff=df_H_p_t[[True if selected_hora in l  else False for l in df_H_p_t.HORAS_POSIBLES ]]
            dff=dff[dff.DIA==selected_dia]
            cond=[dff.UNIDAD=='Facultad de Ciencias Naturales y Matemáticas',dff.UNIDAD=='Facultad de Ingeniería en Electricidad y Computación',dff.UNIDAD=='ESCUELA SUPERIOR POLITECNICA DEL LITORAL',dff.UNIDAD=='Facultad de Ciencias Sociales y Humanísticas',dff.UNIDAD=='Facultad de Ciencias de la Vida']
            resl= ['FCNM','FIEC','ESPOL','FCSH','FCV']
            dff.UNIDAD=np.select(cond,resl)
            dff = dff[['UNIDAD','NOMBRE','HORAINICIO','HORAFIN','PARALELO','COURSE','AULA','CUPOPLANIFICADO']]
            return html.Div([
                html.H4(f'Materias Activas a las {selected_hora}',style={'textAlign':'center'}),
                dash_table.DataTable(
                                    id='table_materias',
                                    columns=[{'name':col, 'id':col}for col in dff.columns],
                                    data=dff.to_dict('records'),  # the contents of the table
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
                                                'fontFamily': 'Quicksand',
                                                },
                                    style_data_conditional = [
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCNM'",
                                                },
                                            'backgroundColor': 'rgb(232, 218, 239)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCSH'",
                                                },
                                            'backgroundColor': 'rgb(252, 243, 207)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'ESPOL'",
                                                },
                                            'backgroundColor': 'rgb(214, 234, 248)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FIEC'",
                                                },
                                            'backgroundColor': 'rgb(214, 219, 223)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCV'",
                                                },
                                            'backgroundColor': 'rgb(209, 242, 235)',
                                            'fontWeight': 'bold'
                                        }]

                ) ],style={'margin':'2vw'})
        else:
            dff=df_H_p_t[df_H_p_t.DIA==selected_dia]
            cond=[dff.UNIDAD=='Facultad de Ciencias Naturales y Matemáticas',dff.UNIDAD=='Facultad de Ingeniería en Electricidad y Computación',dff.UNIDAD=='ESCUELA SUPERIOR POLITECNICA DEL LITORAL',dff.UNIDAD=='Facultad de Ciencias Sociales y Humanísticas',dff.UNIDAD=='Facultad de Ciencias de la Vida']
            resl= ['FCNM','FIEC','ESPOL','FCSH','FCV']
            dff.UNIDAD=np.select(cond,resl)
            dff = dff[['UNIDAD','NOMBRE','HORAINICIO','HORAFIN','PARALELO','COURSE','AULA','CUPOPLANIFICADO']]
            return html.Div([
                html.H4(f'Materias Activas a las {selected_hora}',style={'textAlign':'center'}),
                dash_table.DataTable(
                                    id='table_materias',
                                    columns=[{'name':col, 'id':col}for col in dff.columns],
                                    data=dff.to_dict('records'),  # the contents of the table
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
                                                'fontFamily': 'Quicksand',
                                                },
                                    style_data_conditional = [
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCNM'",
                                                },
                                            'backgroundColor': 'rgb(232, 218, 239)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCSH'",
                                                },
                                            'backgroundColor': 'rgb(252, 243, 207)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'ESPOL'",
                                                },
                                            'backgroundColor': 'rgb(214, 234, 248)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FIEC'",
                                                },
                                            'backgroundColor': 'rgb(214, 219, 223)',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query':"{UNIDAD} = 'FCV'",
                                                },
                                            'backgroundColor': 'rgb(209, 242, 235)',
                                            'fontWeight': 'bold'
                                        }]

                ) ],style={'margin':'2vw'})
    else:
        if selected_hora!='Todo el día':
            dff = df_H_p_t[df_H_p_t['UNIDAD']==selected_facultad]
            dff=dff[[True if selected_hora in l  else False for l in dff.HORAS_POSIBLES ]]
            dff=dff[dff.DIA==selected_dia]
            dff = dff[['NOMBRE','HORAINICIO','HORAFIN','PARALELO','COURSE','AULA','CUPOPLANIFICADO']]
            color = colores_f[selected_facultad]
            return html.Div([
                html.H4(f'Materias Activas a las {selected_hora} ',style={'textAlign':'center'}),
                dash_table.DataTable(
                                    id='table_materias',
                                    columns=[{'name':col, 'id':col}for col in dff.columns],
                                    data=dff.to_dict('records'),  # the contents of the table
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
                                                'fontFamily': 'Quicksand',
                                                },
                                    style_data_conditional = [
                                        {
                                            'if': {
                                                'filter_query':"{PARALELO} > 0",
                                                },
                                            'backgroundColor': color,
                                            'fontWeight': 'bold'
                                        }]
                ) ])
        else:
            dff = df_H_p_t[df_H_p_t['UNIDAD']==selected_facultad]
            dff=dff[dff.DIA==selected_dia]
            dff = dff[['NOMBRE','HORAINICIO','HORAFIN','PARALELO','COURSE','AULA','CUPOPLANIFICADO']]
            color = colores_f[selected_facultad]
            return html.Div([
                html.H4(f'Materias Activas a las {selected_hora} ',style={'textAlign':'center'}),
                dash_table.DataTable(
                                    id='table_materias',
                                    columns=[{'name':col, 'id':col}for col in dff.columns],
                                    data=dff.to_dict('records'),  # the contents of the table
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
                                                'fontFamily': 'Quicksand',
                                                },
                                    style_data_conditional = [
                                        {
                                            'if': {
                                                'filter_query':"{PARALELO} > 0",
                                                },
                                            'backgroundColor': color,
                                            'fontWeight': 'bold'
                                        }]
                ) ])
@app.callback(
    Output('container_flujo','children'),
    [Input('dropdownfacultades', 'value')],
    [Input('dropdown_dia','value')])
def get_linegraph(selected_facul,select_dia):
    df_H_p=pd.read_csv('Dashboard/pages/df_Flujoestudiante.csv')
    if selected_facul == 'Todas las Facultades':
        dff_d = df_H_p[df_H_p.DIA==select_dia]
        dic_horas={}
        for hora in time_30min:
            dic_horas[hora]=0
        for hora in time_30min:
            for cant , list in zip(dff_d.CUPOPLANIFICADO,dff_d.HORAS_POSIBLES):
                if hora in list:
                    dic_horas[hora]+=cant
        df_flujo = pd.DataFrame(columns=['HORAS_POSIBLES','ESTIMADO DE ESTUDIANTES'])
        df_flujo['HORAS_POSIBLES'] = dic_horas.keys()
        df_flujo['ESTIMADO DE ESTUDIANTES'] =dic_horas.values()
        fig = px.line(df_flujo, x="HORAS_POSIBLES", y="ESTIMADO DE ESTUDIANTES")
        fig.update_xaxes(title='HORAS',tickangle=30)
        title = 'Distribucion diaria de aulas por horas correspondiente al dia '
        return html.Div([
                html.H1(f'{title.upper()} {select_dia.upper()}'),
                dcc.Graph(figure=fig),
                html.P('Recordar que para este gráfico solo utiliza el filtrado por Facultad y Dia',style={'margin-left':'2vw','textAlign':'center'}),
            ],style={'margin':'2vw'})
    else:
        dff_d = df_H_p[df_H_p.DIA==select_dia]
        dff_d = dff_d[dff_d.UNIDAD==selected_facul]
        dic_horas={}
        for hora in time_30min:
            dic_horas[hora]=0
        for hora in time_30min:
            for cant , list in zip(dff_d.CUPOPLANIFICADO,dff_d.HORAS_POSIBLES):
                if hora in list:
                    dic_horas[hora]+=cant
        df_flujo = pd.DataFrame(columns=['HORAS_POSIBLES','ESTIMADO DE ESTUDIANTES'])
        df_flujo['HORAS_POSIBLES'] = dic_horas.keys()
        df_flujo['ESTIMADO DE ESTUDIANTES'] =dic_horas.values()
        fig = px.line(df_flujo, x="HORAS_POSIBLES", y="ESTIMADO DE ESTUDIANTES")
        fig.update_xaxes(title='HORAS',tickangle=30)
        return html.Div([
                html.H4(f'AFLUENCIA ESTIMADA DE ESTUDIANTES EN {selected_facul.upper()} CORRESPONDIENTE AL DIA {select_dia.upper()}'),
                dcc.Graph(figure=fig),
                html.P('Recordar que para este gráfico solo utiliza el filtrado por Facultad y Dia',style={'margin-left':'2vw','textAlign':'center'}),
            ])






df_H_p=pd.read_csv('Dashboard/pages/df_Treemap_scatter.csv')
dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves','viernes']
clase_orden = ['Teórico','Práctico']
df_H_p.DIA = pd.Categorical(df_H_p['DIA'], dias_ordenados)
df_H_p.CLASE = pd.Categorical(df_H_p['CLASE'], clase_orden)
df_H_p.sort_values('DIA', inplace=True)
df_H_p.sort_values('CLASE', inplace=True)
cond=[df_H_p['COURSE']==1,df_H_p['COURSE']==2,df_H_p['COURSE']==3,df_H_p['COURSE']==4,df_H_p['COURSE']==5]
res=['COURSE 1','COURSE 2','COURSE 3','COURSE 4','COURSE 5']
df_H_p['COURSE'] = np.select(cond,res,default=df_H_p['COURSE'])
df_H_p['COURSE'] = pd.Categorical(df_H_p['COURSE'], res)
df_H_p.sort_values('COURSE', inplace=True)
h_inicial= dt.datetime(2023, 1, 1, 9, 0, 0)
h_final=dt.datetime(2023, 1, 1, 17, 1, 0)
mediahora=dt.timedelta(minutes=30)
time_30min =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(h_inicial,h_final,mediahora)]
def contruir_condi(n_course,n_clase):
    return (df_H_p['COURSE']== df_H_p.COURSE.unique()[n_course] ) & (df_H_p['CLASE']==df_H_p.CLASE.unique()[n_clase])
   #5 CURSOS Y 2 CLASES [Teórico y Práctico]
cond=[contruir_condi(0,0),contruir_condi(1,0),contruir_condi(2,0),contruir_condi(3,0),contruir_condi(4,0),contruir_condi(0,1),contruir_condi(1,1),contruir_condi(2,1),contruir_condi(3,1),contruir_condi(4,1)]
res=['A','B','C','D','E','F','G','H','I','J']
df_H_p['COLORS'] = np.select(cond,res)
df_H_p['TEXTO1'] = [f'<br>Paralelo: {paralelo}     Aula: {aula} 'for paralelo,aula in zip(df_H_p['PARALELO'],df_H_p['AULA'])]
df_H_p['TEXTO2'] = [f'<br>Hora Entrada: <br> {hi} <br>Hora Salida: <br> {hf}' for hi,hf in zip(df_H_p['HORAINICIO'],df_H_p['HORAFIN'])]  #Hora de entrada y salida
def crear_casos_treemap(materia,facultad):
    dff = df_H_p[df_H_p['UNIDAD']==facultad]
    dff = dff[dff['NOMBRE']==materia]
    fig= px.treemap(dff, path=['NOMBRE', 'COURSE','CLASE','DIA','TEXTO1','TEXTO2'],color='COLORS',maxdepth=4,
                color_discrete_sequence=px.colors.qualitative.Pastel1,color_discrete_map={'A':'rgb(141,211,199)','B':'rgb(190,186,218)','C':'rgb(251,128,114)','D':'rgb(128,177,211)','F':'rgb(253,180,98)','E':'rgb(179,222,105)','G':'rgb(252,205,229)','H':'rgb(217,217,217)','I':'rgb(188,128,189)','J':'rgb(255,237,111)'})
#diseño
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_layout(
        bargap=0.1,
        margin=dict(t=25, b=5, l=5, r=5),
        template='plotly_dark', 
        plot_bgcolor='rgb(255,255,255)',
        paper_bgcolor='rgb(255,255,255)',
        font=dict(
            family="Droid Serif, monospace",
            size=14,
            color="black"))
    return fig
fig_treemap_sistemasdidigitalesI = crear_casos_treemap('SISTEMAS DIGITALES I','Facultad de Ingeniería en Electricidad y Computación')
fig_treemap_principios= crear_casos_treemap('PRINCIPIOS DE ELECTRÓNICA','Facultad de Ingeniería en Electricidad y Computación')
fig_teemap_tecnicas = crear_casos_treemap('TÉCNICAS DIETÉTICAS','Facultad de Ciencias de la Vida')
insights = ['CASOS DE UN SOLO CURSO TEÓRICO Y VARIAS PRÁCTICOS','CLASIFICACIÓN POR TIPO MATERIA','FACULTAD DE CIENCIAS SOCIALES Y HUMANÍSTICAS'
            ,'DISTRIBUCIONES POR FACULTAD','DISTRIBUCIONES POR MATERIA', 'DISTRIBUCIONES POR DOCENTE']
@app.callback(
    Output('Insights_div', 'children'),
    Input('show_insights', 'n_clicks'))
def section_show_insights(clicks_ins):
    if clicks_ins is None:     # hasta que de click
        raise PreventUpdate
    else:
        return  html.Div([
            dcc.Dropdown(insights,'CASOS DE UN SOLO CURSO TEÓRICO Y VARIAS PRÁCTICOS',id='dropwdown_insight'),
        ])
@app.callback(
    Output('container_insight', 'children'),
    Input('dropwdown_insight', 'value'))
def show_insights(value):
    if value == 'CASOS DE UN SOLO CURSO TEÓRICO Y VARIAS PRÁCTICOS':
        df_H_p=pd.read_csv('Dashboard/pages/df_Treemap_scatter.csv')
        dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves','viernes']
        clase_orden = ['Teórico','Práctico']
        df_H_p.DIA = pd.Categorical(df_H_p['DIA'], dias_ordenados)
        df_H_p.CLASE = pd.Categorical(df_H_p['CLASE'], clase_orden)
        df_H_p.sort_values('DIA', inplace=True)
        df_H_p.sort_values('CLASE', inplace=True)
        cond=[df_H_p['COURSE']==1,df_H_p['COURSE']==2,df_H_p['COURSE']==3,df_H_p['COURSE']==4,df_H_p['COURSE']==5]
        res=['COURSE 1','COURSE 2','COURSE 3','COURSE 4','COURSE 5']
        df_H_p['COURSE'] = np.select(cond,res,default=df_H_p['COURSE'])
        df_H_p['COURSE'] = pd.Categorical(df_H_p['COURSE'], res)
        df_H_p.sort_values('COURSE', inplace=True)
        h_inicial= dt.datetime(2023, 1, 1, 9, 0, 0)
        h_final=dt.datetime(2023, 1, 1, 17, 1, 0)
        mediahora=dt.timedelta(minutes=30)
        time_30min =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(h_inicial,h_final,mediahora)]
        def contruir_condi(n_course,n_clase):
            return (df_H_p['COURSE']== df_H_p.COURSE.unique()[n_course] ) & (df_H_p['CLASE']==df_H_p.CLASE.unique()[n_clase])
        #5 CURSOS Y 2 CLASES [Teórico y Práctico]
        cond=[contruir_condi(0,0),contruir_condi(1,0),contruir_condi(2,0),contruir_condi(3,0),contruir_condi(4,0),contruir_condi(0,1),contruir_condi(1,1),contruir_condi(2,1),contruir_condi(3,1),contruir_condi(4,1)]
        res=['A','B','C','D','E','F','G','H','I','J']
        df_H_p['COLORS'] = np.select(cond,res)
        df_H_p['TEXTO1'] = [f'<br>Paralelo: {paralelo}     Aula: {aula} 'for paralelo,aula in zip(df_H_p['PARALELO'],df_H_p['AULA'])]
        df_H_p['TEXTO2'] = [f'<br>Hora Entrada: <br> {hi} <br>Hora Salida: <br> {hf}' for hi,hf in zip(df_H_p['HORAINICIO'],df_H_p['HORAFIN'])]  #Hora de entrada y salida
        def crear_casos_treemap(materia,facultad):
            dff = df_H_p[df_H_p['UNIDAD']==facultad]
            dff = dff[dff['NOMBRE']==materia]
            fig= px.treemap(dff, path=['NOMBRE', 'COURSE','CLASE','DIA','TEXTO1','TEXTO2'],color='COLORS',maxdepth=4,
                        color_discrete_sequence=px.colors.qualitative.Pastel1,color_discrete_map={'A':'rgb(141,211,199)','B':'rgb(190,186,218)','C':'rgb(251,128,114)','D':'rgb(128,177,211)','F':'rgb(253,180,98)','E':'rgb(179,222,105)','G':'rgb(252,205,229)','H':'rgb(217,217,217)','I':'rgb(188,128,189)','J':'rgb(255,237,111)'})
        #diseño
            fig.update_traces(marker=dict(cornerradius=5))
            fig.update_layout(
                bargap=0.1,
                margin=dict(t=25, b=5, l=5, r=5),
                template='plotly_dark', 
                plot_bgcolor='rgb(255,255,255)',
                paper_bgcolor='rgb(255,255,255)',
                font=dict(
                    family="Droid Serif, monospace",
                    size=14,
                    color="black"))
            return fig
        fig_treemap_sistemasdidigitalesI = crear_casos_treemap('SISTEMAS DIGITALES I','Facultad de Ingeniería en Electricidad y Computación')
        fig_treemap_principios= crear_casos_treemap('PRINCIPIOS DE ELECTRÓNICA','Facultad de Ingeniería en Electricidad y Computación')
        fig_teemap_tecnicas = crear_casos_treemap('TÉCNICAS DIETÉTICAS','Facultad de Ciencias de la Vida')

        return html.Div([
            html.H4('CASOS DE UN SOLO CURSO TEÓRICO Y VARIAS PRÁCTICOS'),
            html.Div([
            html.P('Clasificamos por curso:'),
            html.P("Saber que un curso en espol ,la mayoría de veces se compone de una parte teórica y otra parte práctica , por  lo tanto también realizamos su clasificación en una columna llamada 'CLASE', donde solo hay dos valores único o es 'Teórico' o es 'Practico'."),
            html.P("Se puede ver el caso de materias donde existe un solo curso teórico, pero este  a su vez se divide en varios prácticos."),
            html.P("Las materias en cuestión son : "),
            html.P("* Sistemas Digitales I."),
            html.P("* Principios de Electrónica."),
            html.P("* Técnicas Dietéticas."),
            ],style={'textAlign':'justify'}),
            html.Div([
                dcc.Graph(figure=fig_treemap_sistemasdidigitalesI),
                dcc.Graph(figure=fig_treemap_principios),
                dcc.Graph(figure=fig_teemap_tecnicas)
            ])
        ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})
    if value == 'CLASIFICACIÓN POR TIPO MATERIA':
        df_H_p=pd.read_csv('Dashboard/pages/df_Treemap_scatter.csv')
        diferenciar_clase_asindex = df_H_p[['NOMBRE','TIPOMATERIA']].groupby(['NOMBRE','TIPOMATERIA'],as_index=False).count()
        diferenciar_clase= df_H_p[['NOMBRE','TIPOMATERIA']].groupby(['NOMBRE','TIPOMATERIA']).count()
        textteo=''
        textteoprac=''
        for x,y in zip(diferenciar_clase_asindex.NOMBRE,diferenciar_clase_asindex.TIPOMATERIA):
            if y=='teórica':
                textteo+=f'{x}<br>'
            else:
                textteoprac+=f'{x}<br>'
        x= diferenciar_clase.groupby('TIPOMATERIA').value_counts()
        df_tm = pd.DataFrame()
        df_tm['TIPOMATERIA']  = x.index
        df_tm['COUNT'] = x.values
        def get_percentage(unico):
            return ((unico/df_tm['COUNT'].sum())*100).round(2)
        df_tm['PERCENTAGE'] = df_tm['COUNT'].apply(get_percentage)
        df_tm['TEXT'] = [f'{count} --> {percen}%' for count,percen in zip(df_tm['COUNT'],df_tm['PERCENTAGE'])]
        df_tm['TEXT_materias'] = [textteo,textteoprac]
        df_tm.loc[0,'TIPOMATERIA']='TEÓRICA'
        df_tm.loc[1,'TIPOMATERIA']='TEÓRICAPRÁTICA'
        fig_clasificart_p = px.treemap(df_tm,path=['TIPOMATERIA','TEXT_materias'],color='TIPOMATERIA',color_discrete_sequence=px.colors.qualitative.Pastel1,title='CLASIFICACIÓN POR TIPO MATERIA')
        fig_tm = px.bar(df_tm, x='TIPOMATERIA', y='COUNT', text_auto=True,color='TIPOMATERIA',color_discrete_sequence=px.colors.qualitative.Pastel1,title="TIPO DE MATERIA ")
        fig_tm.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        for x,y,z in zip(df_tm['TIPOMATERIA'],df_tm['COUNT'],df_tm['PERCENTAGE']):
            fig_tm.add_annotation(
                x=x
                , y=y+0.4
                , text=f"{z}%"
                , showarrow=False
                , arrowhead=1
                , arrowsize=1
                , arrowwidth=2
                , ax=-20
                , ay=-30
                , font=dict(size=12, color="black")
                ,)
        return html.Div([
            html.H4('CLASIFICACIÓN POR TIPO MATERIA'),
            html.Div([
            html.P('Permite ver la distribución de por tipo de materias disponibles en el PAE 2023 '),
            html.P("Saber que existen dos tipos: "),
            html.P("Se puede ver el caso de materias donde existe un solo curso teórico, pero este  a su vez se divide en varios prácticos."),
            html.P("Las materias en cuestión son : "),
            html.P("* Teórica"),
            html.P("* TeóricoPráctica"),
            html.P("Ademas se puede ver el porcentaje que representa del total."),
            ],style={'textAlign':'justify'}),
            html.Div(id='container_tabla_clasi'),
            dcc.Graph(figure=fig_clasificart_p),
            dcc.Graph(figure=fig_tm)
        ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})
    if value == 'FACULTAD DE CIENCIAS SOCIALES Y HUMANÍSTICAS':
        h_inicial= dt.datetime(2023, 1, 1, 9, 0, 0)
        h_final=dt.datetime(2023, 1, 1, 17, 1, 0)
        mediahora=dt.timedelta(minutes=30)
        time_30min =[(str(x).split('T')[1]).split('.')[0] for x in np.arange(h_inicial,h_final,mediahora)]
        dff=df_H_p_t[[True if '14:00:00' in l  else False for l in df_H_p_t.HORAS_POSIBLES ]]
        def get_linegraph(select_dia):
            df_H_p=pd.read_csv('Dashboard/pages/df_Flujoestudiante.csv')
            dff_d = df_H_p[df_H_p.DIA==select_dia]
            dff_d = dff_d[dff_d.UNIDAD=='Facultad de Ciencias Sociales y Humanísticas']
            dic_horas={}
            for hora in time_30min:
                dic_horas[hora]=0
            for hora in time_30min:
                for cant , list in zip(dff_d.CUPOPLANIFICADO,dff_d.HORAS_POSIBLES):
                    if hora in list:
                        dic_horas[hora]+=cant
            df_flujo = pd.DataFrame(columns=['HORAS_POSIBLES','ESTIMADO DE ESTUDIANTES'])
            df_flujo['HORAS_POSIBLES'] = dic_horas.keys()
            df_flujo['ESTIMADO DE ESTUDIANTES'] =dic_horas.values()
            fig = px.line(df_flujo, x="HORAS_POSIBLES", y="ESTIMADO DE ESTUDIANTES")
            fig.update_layout(
            title={
            'text' :f'{select_dia.upper()}',
            'x':0.5,
            'xanchor': 'center'
        })
            fig.update_xaxes(title='HORAS',tickangle=90)
            return fig
        lunes= get_linegraph('lunes')
        martes= get_linegraph('martes')
        miércoles = get_linegraph('miércoles')
        jueves = get_linegraph('jueves')
        return html.Div([
            html.Div([
                html.H4('FACULTAD DE CIENCIAS SOCIALES Y HUMANÍSTICAS'),
                html.Div([html.P("En los gráficos se pudo observar que todas sus materia reciben clases a partir de las 14:00:00 pm hasta las 17:00:00pm"),
                html.P("Las materias  que se reciben aquí son todos los niveles de Ingles"),
                html.P("* Todas las materias de ingles que incluso son todas las que pertenecen a esta facultad entran y salen a la misma hora"),
                html.P("* Solo tienen clase de Lunes a Miércoles"),],style={'textAlign':'justify'}),
                html.Img(src='../Dashboard/assets/Imagenes_slytheryn/FCSH.png'),
                html.Div([dcc.Graph(figure=lunes,style={'width':'40vw'}),
                dcc.Graph(figure=martes,style={'width':'40vw'})],style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center",'margin':'2vw'}),
                html.Div([dcc.Graph(figure=miércoles,style={'width':'40vw'}),
                dcc.Graph(figure=jueves,style={'width':'40vw'})],style={"display": "flex",'flex-direction':'row',"justify-content": "center","align-items": "center",'margin':'2vw'})

            ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})
            ],style={'display':'flex'})
    df_create_tables  = pd.read_csv('Dashboard/pages/df_Createtables.csv')
    cond=[df_create_tables.UNIDAD=='Facultad de Ciencias Naturales y Matemáticas',df_create_tables.UNIDAD=='Facultad de Ingeniería en Electricidad y Computación',df_create_tables.UNIDAD=='ESCUELA SUPERIOR POLITECNICA DEL LITORAL',df_create_tables.UNIDAD=='Facultad de Ciencias Sociales y Humanísticas',df_create_tables.UNIDAD=='Facultad de Ciencias de la Vida']
    resl= ['FCNM','FIEC','ESPOL','FCSH','FCV']
    df_create_tables.UNIDAD=np.select(cond,resl)
    df_filter = df_create_tables[['UNIDAD', 'NOMBRE', 'PARALELO','CLASE', 'CUPOPLANIFICADO']].groupby(['UNIDAD', 'NOMBRE','PARALELO','CLASE','CUPOPLANIFICADO'], as_index=False).count()
    if value=='DISTRIBUCIONES POR FACULTAD':
        top7_paralelo_moststudents = df_filter.sort_values('CUPOPLANIFICADO', ascending=False).iloc[:7].reset_index(drop=True)
        paralelos_faculty = df_filter[['UNIDAD']].groupby(['UNIDAD'], as_index=False).value_counts().rename(columns={'count':'TOTALPARALELOS'}).sort_values('TOTALPARALELOS', ascending=False)
        def get_percentage(unico):
            return ((unico/paralelos_faculty['TOTALPARALELOS'].sum())*100).round(2)
        paralelos_faculty['PERCENTAGE'] = paralelos_faculty['TOTALPARALELOS'].apply(get_percentage)
        fig_paralelos_faculty= px.bar(paralelos_faculty, x = 'UNIDAD', y = 'TOTALPARALELOS', text_auto=True,title='DISTRIBUCIONES DE PARALELOS POR FACULTAD',color='UNIDAD',color_discrete_map={
            'FIEC' :'rgb(118, 150, 170)',
            'FCV':'rgb(0, 185, 67)',
            'FCNM' :'rgb(100, 64, 155)',
            'FCSH':'rgb(255,180,0)',
            'ESPOL':'rgb(27, 174, 229)'
        })
        for x,y,z in zip(paralelos_faculty['UNIDAD'],paralelos_faculty['TOTALPARALELOS'],paralelos_faculty['PERCENTAGE']):
            fig_paralelos_faculty.add_annotation(
                x=x
                , y=y+2
                , text=f"{z}%"
                , showarrow=False
                , arrowhead=1
                , arrowsize=1
                , arrowwidth=2
                , ax=-20
                , ay=-30
                , font=dict(size=12, color="black")
                ,)
        fig_paralelos_faculty.update_traces(textfont_size=11, textangle=0, textfont_color='black',textposition="inside" ,cliponaxis=False)
        fig_paralelos_faculty.update_xaxes(title='FACULTADES')
        fig_paralelos_faculty.update_yaxes(title='TOTAL PARALELOS')
        df_unidad_cupo = df_filter.drop(columns=['PARALELO', 'CLASE', 'NOMBRE'])
        students_per_faculty = df_unidad_cupo.groupby(['UNIDAD'], as_index=False).sum(numeric_only=True).sort_values("CUPOPLANIFICADO", ascending=False).reset_index(drop=True)
        def get_percentage(unico):
            return ((unico/students_per_faculty['CUPOPLANIFICADO'].sum())*100).round(2)
        students_per_faculty['PERCENTAGE'] = students_per_faculty['CUPOPLANIFICADO'].apply(get_percentage)
        fig_students_per_faculty = px.bar(students_per_faculty, x='UNIDAD', y='CUPOPLANIFICADO', text_auto=True,title='DISTRIBUCIÓN DE ESTUDIANTES POR FACULTAD',color='UNIDAD',color_discrete_map={
            'FIEC' :'rgb(118, 150, 170)',
            'FCV':'rgb(0, 185, 67)',
            'FCNM' :'rgb(100, 64, 155)',
            'FCSH':'rgb(255,180,0)',
            'ESPOL':'rgb(27, 174, 229)'
        })
        for x,y,z in zip(students_per_faculty['UNIDAD'],students_per_faculty['CUPOPLANIFICADO'],students_per_faculty['PERCENTAGE']):
            fig_students_per_faculty.add_annotation(
                x=x
                , y=y+60
                , text=f"{z}%"
                , showarrow=False
                , arrowhead=1
                , arrowsize=1
                , arrowwidth=2
                , ax=-20
                , ay=-30
                , font=dict(size=12, color="black")
                ,)
        fig_students_per_faculty.update_traces(textfont_size=11, textangle=0, textfont_color='black',textposition="inside" ,cliponaxis=False)
        fig_students_per_faculty.update_xaxes(title='FACULTADES')
        fig_students_per_faculty.update_yaxes(title='CUPO PLANIFICADO')
        paralelos_faculty_dia = df_create_tables[['UNIDAD', 'NOMBRE', 'BLOQUE', 'PARALELO', 'DIA', 'CUPOPLANIFICADO']].groupby(['UNIDAD', 'NOMBRE', 'BLOQUE', 'PARALELO', 'DIA', 'CUPOPLANIFICADO'], as_index=False).count()
        df_paralelos_faculty_dia = paralelos_faculty_dia[['UNIDAD', 'DIA']].groupby(['UNIDAD', 'DIA'], as_index=False).value_counts().sort_values('count', ascending=False).rename(columns={'count':'TOTAL'})
        fig_paralelos_faculty_dia  = px.bar(df_paralelos_faculty_dia , x ='DIA', y = 'TOTAL', color='UNIDAD', barmode='group', text_auto=True, title='DISTRIBUCIÓN DE PARALELOS POR FACULTAD Y DÍA',color_discrete_map={
            'FIEC' :'rgb(118, 150, 170)',
            'FCV':'rgb(0, 185, 67)',
            'FCNM' :'rgb(100, 64, 155)',
            'FCSH':'rgb(255,180,0)',
            'ESPOL':'rgb(27, 174, 229)'
        })
        fig_paralelos_faculty_dia.update_traces(textfont_size=11, textangle=0, textfont_color='black',textposition="outside" ,cliponaxis=False)
        fig_paralelos_faculty_dia.update_xaxes(categoryarray=['lunes','martes','miércoles','jueves'])
        fig_paralelos_faculty_dia.update_xaxes(title='DIAS')
        fig_paralelos_faculty_dia.update_yaxes(title='PARALELOS')
        boxplot_paralelos_day = px.box(df_paralelos_faculty_dia, y="TOTAL", x='DIA', color="DIA",
            boxmode="overlay", points='all',color_discrete_sequence=px.colors.qualitative.Set1,title='DISTRIBUCION DE PARALELOS POR DIA')
        boxplot_paralelos_day.update_traces(boxmean=True, selector=dict(type='box'))
        boxplot_paralelos_day.update_xaxes(categoryarray=['lunes','martes','miércoles','jueves'])
        boxplot_paralelos_day.update_xaxes(title='DÍAS')
        
        return html.Div([
            html.Div([
                html.H4('TOP 7 PARALELOS CON MÁS CUPOS'),
                html.Div([
                    html.P("Muestra el top 7 de los paralelos con más cupos en ESPOL en el PAE  "),
                    html.P("A destacar:"),
                    html.P("* La facultad con paralelos con más cupos es la llamada ESCUELA SUPERIOR POLITECNICA DEL LITORAL"),
                    html.P("* La materia con más paralelos es EMPRENDIMIENTO E INNOVACIÓN"),],style={'textAlign':'jusitfy'}),
                    dash_table.DataTable(
                        top7_paralelo_moststudents.to_dict('records'),
                        [{'name': i, 'id': i} for i in top7_paralelo_moststudents.columns],
                        cell_selectable=True,  # para que no se me presente el hover
                        fill_width=False,
                        sort_action='native',
                        style_as_list_view=True,
                        style_header={
                            'backgroundColor': '#edf3f4',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'backgroundColor': '#edf3f4',
                            'textAlign': 'center',
                            'padding': '5px'
                        },
                        style_data={'borderBottom': '1px solid #167ac6',
                                    'fontFamily': 'Quicksand',
                                    },
                        style_data_conditional = [
                                                {
                                                    'if': {
                                                        'filter_query':"{UNIDAD} = 'FCNM'",
                                                        },
                                                    'backgroundColor': 'rgb(232, 218, 239)',
                                                    'fontWeight': 'bold'
                                                },
                                                {
                                                    'if': {
                                                        'filter_query':"{UNIDAD} = 'FCSH'",
                                                        },
                                                    'backgroundColor': 'rgb(252, 243, 207)',
                                                    'fontWeight': 'bold'
                                                },
                                                {
                                                    'if': {
                                                        'filter_query':"{UNIDAD} = 'ESPOL'",
                                                        },
                                                    'backgroundColor': 'rgb(214, 234, 248)',
                                                    'fontWeight': 'bold'
                                                },
                                                {
                                                    'if': {
                                                        'filter_query':"{UNIDAD} = 'FIEC'",
                                                        },
                                                    'backgroundColor': 'rgb(214, 219, 223)',
                                                    'fontWeight': 'bold'
                                                },
                                                {
                                                    'if': {
                                                        'filter_query':"{UNIDAD} = 'FCV'",
                                                        },
                                                    'backgroundColor': 'rgb(209, 242, 235)',
                                                    'fontWeight': 'bold'
                                                }])
            ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"}),
            html.Div([
                html.H4('DISTRIBUCIONES DE PARALELOS POR FACULTAD',style={'margin-top':'2vw'}),
                html.Div([
                    html.P("Muestra la distribución de los paralelos por facultad"),
                    html.P("A destacar:"),
                    html.P("* La facultad con más paralelos es la llamada ESCUELA SUPERIOR POLITECNICA DEL LITORAL "),
                    html.P("* La facultad con menos paralelos es la llamada Facultad de Ciencias de la Vida"),],style={'textAlign':'jusitfy'}),
                dcc.Graph(figure=fig_paralelos_faculty,style={'width':'100%','height':'100%'})
            ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"}),
            html.Div([
                html.H4('DISTRIBUCIÓN DE ESTUDIANTES POR FACULTAD'),
                html.Div([
                    html.P("Muestra el total de estudiantes por cada facultad en ESPOL en el PAE"),
                    html.P("A destacar:"),
                    html.P("* La facultad  con más cupos es 'Facultad de Ciencias Sociales y Humanísticas "),
                    html.P("* La facultad  con menos cupos es 'Facultad de Ciencias de la Vida"),
                    html.P("* La media de cupos por facultad es 338.6"),
                    html.P("* La facultad 'Facultad de Ciencias Sociales y Humanísticas'tiene una demanda excesiva de cupos "),],style={'textAlign':'jusitfy'}),
                dcc.Graph(figure=fig_students_per_faculty,style={'width':'100%','height':'100%'})
            ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"}),
            html.Div([
                html.H4('DISTRIBUCIONES DE PARALELOS POR FACULTAD Y DIA',style={'margin-top':'2vw'}),
                html.Div([
                    html.P("Muestra la distribución de los paralelos por facultad"),
                    html.P("A destacar:"),
                    html.P("* La facultad con más paralelos es la llamada ESCUELA SUPERIOR POLITECNICA DEL LITORAL "),
                    html.P("* La facultad con menos paralelos es la llamada Facultad de Ciencias de la Vida"),],style={'textAlign':'jusitfy'}),
                dcc.Graph(figure=fig_paralelos_faculty_dia,style={'width':'100%','height':'100%'}),
                dcc.Graph(figure= boxplot_paralelos_day,style={'width':'100%','height':'100%'}),
            ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"}),
        ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})
    if value=='DISTRIBUCIONES POR MATERIA':
        top_most_paralelos_clase = df_filter[['UNIDAD', 'NOMBRE','CLASE']].groupby(['UNIDAD', 'NOMBRE','CLASE'], as_index=False).value_counts().sort_values('count', ascending=False).rename(columns={'count':'PARALELOS'})
        top_most_paralelos = df_filter[['UNIDAD', 'NOMBRE']].groupby(['UNIDAD', 'NOMBRE'], as_index=False).value_counts().sort_values('count', ascending=False).rename(columns={'count':'PARALELOS'})
        top_most_paralelos=top_most_paralelos.iloc[0:10]
        xaxes = top_most_paralelos.NOMBRE
        top_most_paralelos=top_most_paralelos_clase[np.isin(top_most_paralelos_clase.NOMBRE,top_most_paralelos.NOMBRE)]
        fig_top_most_paralelos= px.bar(top_most_paralelos, x = 'NOMBRE', y='PARALELOS',color ='CLASE',barmode='group', text_auto=True, color_discrete_sequence=px.colors.qualitative.Pastel1,
                                    title='TOP 10 MATERIAS CON MÁS PARALELOS')
        fig_top_most_paralelos.update_xaxes(title='MATERIAS')
        fig_top_most_paralelos.update_xaxes(categoryarray=xaxes)
        return html.Div([
            html.H4('TOP 10 MATERIAS CON MÁS PARALELOS'),
            html.Div([
                dcc.Graph(figure =fig_top_most_paralelos),
            ])],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})
    if value=="DISTRIBUCIONES POR DOCENTE":
        df_duracion_fomattime=pd.read_csv('Dashboard/pages/df_duracion_fomattime.csv')
        df_duracion_fomattime['HORAINICIO'] = pd.to_datetime(df_duracion_fomattime['HORAINICIO'],format="%I:%M:%S%p")
        df_duracion_fomattime['HORAFIN'] = pd.to_datetime(df_duracion_fomattime['HORAFIN'],format="%I:%M:%S%p")
        df_duracion_fomattime['DURACION'] = (df_duracion_fomattime['HORAFIN']-df_duracion_fomattime['HORAINICIO'])
        df_duracion_fomattime['HORAINICIO'] = [dt.datetime.strptime(str(t),'%Y-%m-%d %H:%M:%S').time() for  t in df_duracion_fomattime['HORAINICIO']]
        df_duracion_fomattime['HORAFIN'] = [dt.datetime.strptime(str(t),'%Y-%m-%d %H:%M:%S').time() for  t in df_duracion_fomattime['HORAFIN']]
        df_duracion = df_duracion_fomattime[['DOCENTE','DURACION']].groupby(['DOCENTE']).sum().sort_values('DURACION')
        df_duracion['DURACION'] = [(str(d).split('s')[1].strip()) for d in df_duracion['DURACION']]
        duraciones_unicas = df_duracion.DURACION.unique()
        table_duracion = pd.DataFrame(df_duracion['DURACION'].value_counts())
        fig_teachers_duracion = px.bar(table_duracion,x=table_duracion.index,y='count',color=table_duracion.index ,color_discrete_sequence=px.colors.qualitative.Pastel2,text_auto=True )
        fig_teachers_duracion .update_traces(textfont_size=11, textangle=0, textfont_color='black',textposition="outside" ,cliponaxis=False)
        fig_teachers_duracion.update_yaxes(title='NUMERO DE DOCENTES')
        fig_teachers_duracion.update_xaxes(title='CARGA HORARIA',categoryarray=duraciones_unicas) 
        lista_text_duracion = ['']*len(duraciones_unicas)
        l_duraciones_unicas= duraciones_unicas.tolist()
        table_duracion['TEXT']=lista_text_duracion
        for docente,duracion in zip(df_duracion.index,df_duracion.DURACION):
            pos= l_duraciones_unicas.index(duracion)
            table_duracion.loc[duracion,'TEXT'] += docente + '<br>'
        fig_teachers_duracion_icicle =px.icicle(table_duracion,path=[px.Constant('DURACIONES'),table_duracion.index,'count','TEXT'],maxdepth=3)
        fig_teachers_duracion_icicle.update_traces(root_color="lightgrey")
        fig_teachers_duracion_icicle.update_traces(
            hovertemplate='')
        fig_teachers_duracion_icicle.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        return html.Div([
            html.H4('DISTRIBUCION DE CANTIDAD DE DOCENTES POR CARGA HORARIA SEMANAL'),
            dcc.Graph(figure=fig_teachers_duracion),
            dcc.Graph(figure=fig_teachers_duracion_icicle)
        ],style={"display": "flex",'flex-direction':'column',"justify-content": "center","align-items": "center"})