import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html,callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import os 
from pages import Argentina, Australia,Belgium,Brazil,Canada,Cameroon,Costa_Rica,Croatia, Denmark, Ecuador,England,Spain,France,Germany,Ghana,Iran,Japan,Korea_Republic,Saudi_Arabic,Morocco,Mexico,Netherlands,Poland,Portugal,Qatar,Senegal,Serbia,Switzerland,Tunisia,Uruguay,United_States,Wales,Confederations,home1


# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py

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
                href="https://www.fifa.com/es",
                style={"textDecoration": "none"},
            ),
            html.A(
                dbc.Row(
                    [
                        html.P('CONFEDERATIONS'),
                    ],
                    align="center",
                    className="g-0", 
                ),
                href="/Confederations",
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

@callback(
    Output("navbar-collapse", "is_open",),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
        {"key": "2", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
        {"key": "3", "src": "https://www.un.org/sites/un2.un.org/files/fftg_web_banner_s.png"},
    ],
    controls=True,
    indicators=True,
    interval=2000,
    ride="carousel"
)
#Hay 5 confederaciones 
folder_images = 'assets/Selecciones'
folder_confe = 'assets/Confederaciones'
df_img_team = pd.read_csv('DASHBOARD/assets/datas/selecciones.csv',sep=';')
def contruir_seccion_confederation(df):
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
    return UEFA,AFC,CAF,CONMEBOL,CONCACAF
UEFA,AFC,CAF,CONMEBOL,CONCACAF = contruir_seccion_confederation(df_img_team)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
    [navbar,UEFA,AFC,CAF,CONMEBOL,CONCACAF])
])

