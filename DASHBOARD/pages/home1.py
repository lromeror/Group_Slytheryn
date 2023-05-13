import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os

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
            dcc.Link(
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
    Output("navbar-collapse", "is_open",allow_duplicate=True),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
    prevent_initial_call=True,
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

space_im=dbc.Row(
    
      [  #dbc.Col(html.Img(src='https://ep00.epimg.net/deportes/imagenes/2014/07/13/album/1405277136_956299_1405330813_album_normal.jpg' ,className='img-fluid')),
        #dbc.Col(html.Img(src='../../PROYECTOESPOL/img/cmp2.jpg')),
        dbc.Col(html.Img(src="foto\cmp3.jpg"))]   

)
#folder=r"C:/Users/Jonanyu 11.1/Desktop/img"
#os.path.join(folder,"cm1.jpg")
layout = html.Div(
    [navbar, carousel,space_im]
    #html.Img(children=os.path.join(folder,"cm1.jpg"))
    
)