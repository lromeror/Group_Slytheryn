import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os
import pandas as pd


nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))



FIFA_LOGO = "https://cdn.cookielaw.org/logos/a22264f8-9d14-4ab8-ab4b-a61925d0e901/6b589592-a31b-4ede-9440-c6368b1eb13b/d0426540-ceee-4ccb-b321-ac2656d493bb/fcm_rgbf_s.png"

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

navbar1 = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=FIFA_LOGO, height="40px")),
                        dbc.Col(dbc.NavbarBrand("", className="ms-2")),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=20),
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

@callback(
    Output("navbar-collapse", "is_open",allow_duplicate=True),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
    prevent_initial_call='initial_duplicate'
)
def toggle_navbar_collapse(n, is_open):

    if n:
        return not is_open
    return is_open

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


navbar2 = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Home",href= "/home1",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Confederations",href= "/Confederations",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Statistics",href= "/Estadisticas",style={"textDecoration": "none"})),
                        #dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"),className="right"),
                        
                    ],
                    align="right",
                    className="g-0",
                ),
                #href="https://plotly.com",
                #style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
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

@callback(
    Output("navbar-collapse1", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

carousel = dbc.Carousel(
    items=[
        {"key": "1", 
         "src": "https://images2.minutemediacdn.com/image/upload/c_crop,w_4020,h_2261,x_0,y_110/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/12up_es_international_web/01gmk9xqdff9tjvhar8g.jpg"
         },
        {"key": "2", "src": "https://resizer.iproimg.com/unsafe/880x/filters:format(webp)/https://assets.iproup.com/assets/jpg/2023/03/34125.jpg"},
        {"key": "3", "src": "https://cdn.mos.cms.futurecdn.net/Uy2oLCTFTGAFbUp5mg2Q3H.jpg"},
    ],
    controls=True,
    indicators=True,
    interval=3000,
    ride="carousel",
    className='img-fluid'
)

folder_images = 'assets/Selecciones'

folder_confe = 'assets/Confederaciones'
df_img_team = pd.read_csv('DASHBOARD/assets/datas/selecciones.csv',sep=',')


<<<<<<< HEAD

def imagenes_confe(df):
    for confederation in df.continente.unique():
        df_f = df[df.continente==confederation]
        teams_per_confe = df_f.team.unique() 
        
        if confederation == 'UEFA':
            imagenes = []
            for img in range(len(teams_per_confe)):
                imag={
                    'src': os.path.join(folder_images,teams_per_confe[img]),
                    'alt': 'Imagen '+str(img),    
                }
                imagenes.append(imag)
                
            UEFA = dbc.Container([dbc.Row(
                     [
                    dbc.Col(
                     html.Img(src=imagen['src'], alt=imagen['alt'], className="img-fluid"),
                    sm=6, md=4, lg=3, # Define el tamaño de la columna según el ancho de la pantalla
                    className="mb-4 ",
                    )
                for imagen in imagenes
                         ],
                    className="  row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-0 ", # Define el número de columnas en diferentes tamaños de pantalla
                    )], className="justify-content-center")
    return UEFA


"""def contruir_seccion_confederation(df):
    for confederation in df.continente.unique(): #en el data set la columna continente esta la clasificacion por confederación
        df_f = df[df.continente==confederation]
        teams_per_confe = df_f.team.unique()    # codigo de los equipos para las imagenes
        name_teams_per_confe = df_f.seleccion.unique()  # nombre de los equipos
        if confederation == 'UEFA':   # 13 teams
            UEFA = dbc.Row([
                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
                                html.H4('EUROPA'),
                                html.P('Union des associations européennes de football (UEFA)')],className="container_federation"),
                        dbc.Col([             
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[5]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[5].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[5].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[6]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[6].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[6].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[7]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[7].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[7].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[8]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[8].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[8].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[9]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[9].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[9].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[10]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[10].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[10].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[11]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[11].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[11].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[12]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[12].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[12].title()}"),
                                ],className='d-flex flex-row flex-wrap w-75')
                    ],className='d-flex justify-content-md-center container_principal_images')
        if confederation == 'AFC': 
            AFC = dbc.Row([
                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
                                html.H4('ASIA'),
                                html.P('Confédération Africaine de Football (CAF)')],className="container_federation"),
                        dbc.Col([             
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[5]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[5].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[5].title()}"),
                                ],className='d-flex flex-row flex-wrap w-75')
                    ],className='d-flex justify-content-md-center container_principal_images')
        if confederation == 'CAF': 
            CAF = dbc.Row([
                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
                                html.H4('AFRICA'),
                                html.P('Asian Football Confederation (AFC)')],className="container_federation"),
                        dbc.Col([             
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
                                ],className='d-flex flex-row flex-wrap w-75')
                    ],className='d-flex justify-content-md-center container_principal_images')
        if confederation == 'CONMEBOL':
            CONMEBOL = dbc.Row([
                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
                                html.H4('SUDAMERICA'),
                                html.P('Confederación Sudamericana de Fútbol (CONMEBOL)')],className="container_federation"),
                        dbc.Col([             
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
                                ],className='d-flex flex-row flex-wrap w-75')
                    ],className='d-flex justify-content-md-center container_principal_images')
        if confederation == 'CONCACAF':
            CONCACAF = dbc.Row([
                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
                                html.H4('NORTE AMERICA'),
                                html.P('The Confederation of North, Central America and Caribbean Association (CONCACAF)')],className="container_federation"),
                        dbc.Col([             
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
                                ],className='d-flex flex-row flex-wrap w-75')
                    ],className='d-flex justify-content-md-center container_principal_images')
    return UEFA,AFC,CAF,CONMEBOL,CONCACAF"""
UEFA = imagenes_confe(df_img_team)


layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Container(
    [navbar1, navbar2,carousel,UEFA],className="")
=======
#navbarConfederations = dbc.Navbar(
#    dbc.Container(
#        [
#            dbc.Row(
#                [
#                    dbc.Col(html.H3("Confederaciones"), className="navbar-brand mx-auto"),
#                    dbc.Col( html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#            )],
#                className="align-items-center",
#                style={"height": "100%"},
#            ),
#        ],
#        fluid=True,
#    ),
#    color="dark",
#    dark=True,
#)
#
#
#def contruir_seccion_confederation(df):
#    for confederation in df.continente.unique(): #en el data set la columna continente esta la clasificacion por confederación
#        df_f = df[df.continente==confederation]
#        teams_per_confe = df_f.team.unique()    # codigo de los equipos para las imagenes
#        name_teams_per_confe = df_f.seleccion.unique()  # nombre de los equipos
#        if confederation == 'UEFA':   # 13 teams
#            UEFA = dbc.Row([
#                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#                                html.H4('EUROPA'),
#                                html.P('Union des associations européennes de football (UEFA)')],className="container_federation"),
#                        dbc.Col([             
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[5]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[5].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[5].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[6]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[6].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[6].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[7]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[7].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[7].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[8]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[8].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[8].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[9]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[9].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[9].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[10]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[10].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[10].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[11]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[11].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[11].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[12]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[12].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[12].title()}"),
#                                ],className='d-flex flex-row flex-wrap w-75')
#                    ],className='d-flex justify-content-md-center container_principal_images')
#        if confederation == 'AFC': 
#            AFC = dbc.Row([
#                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#                                html.H4('ASIA'),
#                                html.P('Confédération Africaine de Football (CAF)')],className="container_federation"),
#                        dbc.Col([             
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[5]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[5].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[5].title()}"),
#                                ],className='d-flex flex-row flex-wrap w-75')
#                    ],className='d-flex justify-content-md-center container_principal_images')
#        if confederation == 'CAF': 
#            CAF = dbc.Row([
#                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#                                html.H4('AFRICA'),
#                                html.P('Asian Football Confederation (AFC)')],className="container_federation"),
#                        dbc.Col([             
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[4]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[4].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[4].title()}"),
#                                ],className='d-flex flex-row flex-wrap w-75')
#                    ],className='d-flex justify-content-md-center container_principal_images')
#        if confederation == 'CONMEBOL':
#            CONMEBOL = dbc.Row([
#                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#                                html.H4('SUDAMERICA'),
#                                html.P('Confederación Sudamericana de Fútbol (CONMEBOL)')],className="container_federation"),
#                        dbc.Col([             
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
#                                ],className='d-flex flex-row flex-wrap w-75')
#                    ],className='d-flex justify-content-md-center container_principal_images')
#        if confederation == 'CONCACAF':
#            CONCACAF = dbc.Row([
#                        dbc.Col([ html.Img(src=os.path.join(folder_confe,confederation+'.png'),className='img_confederation'),
#                                html.H4('NORTE AMERICA'),
#                                html.P('The Confederation of North, Central America and Caribbean Association (CONCACAF)')],className="container_federation"),
#                        dbc.Col([             
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[0]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[0].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[0].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[1]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[1].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[1].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[2]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[2].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[2].title()}"),
#                                dcc.Link([html.Div([html.Img(src=os.path.join(folder_images,teams_per_confe[3]),className='img_team'),
#                                html.H5(f"{name_teams_per_confe[3].title()}")],className='container_img_name')],href=f"/{name_teams_per_confe[3].title()}"),
#                                ],className='d-flex flex-row flex-wrap w-75')
#                    ],className='d-flex justify-content-md-center container_principal_images')
#    return UEFA,AFC,CAF,CONMEBOL,CONCACAF
#UEFA,AFC,CAF,CONMEBOL,CONCACAF = contruir_seccion_confederation(df_img_team)
#

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
    [navbar1, navbar2])
>>>>>>> c026083716ff4767b9e6ba3ed184e8b5e4395a7e
])

