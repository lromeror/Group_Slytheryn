import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import os
import plotly.express as px
import pandas as pd



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
                        dbc.Col(dbc.NavbarBrand("Statistics",href= "/Estadisticas",style={"textDecoration": "none"})),
                        dbc.Col(dbc.NavbarBrand("Comparations",href= "/Comparations",style={"textDecoration": "none"})),
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


folder_images = 'assets/Selecciones'
folder_confe = 'assets/Confederaciones'
df_img_team = pd.read_csv('DASHBOARD/assets/datas/selecciones.csv',sep=',')

carousel = dbc.Carousel(
    items=[
        {"key": "1", 
         "src": os.path.join(folder_images,"foto1.png")
         },
        {"key": "2", "src": os.path.join(folder_images,"foto2.png")},
        {"key": "3", "src": os.path.join(folder_images,"foto3.png")},
    ],
    controls=True,
    indicators=True,
    interval=3000,
    ride="carousel",
    className='img-fluid'
)

def imagenes_confe(df):
    for confederation in df.continente.unique():
        df_f = df[df.continente==confederation]
        teams_per_confe = df_f.team.unique()
        if confederation == 'UEFA':
            UEFA= html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                            dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(src=os.path.join(folder_confe,confederation+".png"), style={"width": "200px", "height": "150px",'border-radius': '5px'}),
                        html.Br(),
                        html.H3("Union of European Football Associations"),
                    ],
                    width=4
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[0]), alt="Logo 1", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[1]), alt="Logo 2", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[2]), alt="Logo 3", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[3]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[4]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[5]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0")]
                        ),dbc.Row(
            [
                dbc.Col(html.Div(style={'height': '10px'}))
            ]
        ),
                        dbc.Row(
                            [
                                
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[6]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[7]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[8]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[9]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[10]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[11]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    ]
                        ),
                        dbc.Row(
            [
                dbc.Col(html.Div(style={'height': '10px'}))
            ]
        ),dbc.Row(
                            [
                                dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[12]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    ]
                        )
        
                    ],
                    width=8
                ),
            ]
        )
                        ],
                        className="my-4",
                        style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )
        elif confederation == 'AFC':
            AFC= html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                            dbc.Row(
                                dbc.Col(
                                    [
                                        html.Img(src=os.path.join(folder_confe,confederation+".png"), alt="Logo", style={"width": "200px", "height": "150px",'border-radius': '5px'}),
                                        html.Br(),html.Br(),
                                        html.H4("Asian Football Confederation"),
                                    ],
                                    className="text-center"
                                )
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[0]), alt="Logo 1", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[1]), alt="Logo 2", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[2]), alt="Logo 3", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[3]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[4]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[5]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0")
                                 
                                ],
                                className="mt-4 no-gutters justify-content-center  g-0",
                            ),
                        ],
                        className="my-4",
                        style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )
        elif confederation == 'CONMEBOL':
            CONMEBOL= html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                            dbc.Row(
                                dbc.Col(
                                    [
                                        html.Img(src=os.path.join(folder_confe,confederation+".png"), alt="Logo", style={"width": "200px", "height": "150px",'border-radius': '5px'}),
                                        html.Br(),html.Br(),
                                        html.H4("The organization for football in South America"),html.Br(),
                                    ],
                                    className="text-center"
                                )
                            ),
                            dbc.Row(
                                [   
                                    
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[0]), alt="Logo 1", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[1]), alt="Logo 2", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[2]), alt="Logo 3", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[3]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    
                                 
                                ],
                                className="mt-4 no-gutters justify-content-center",
                            ),
                        ],
                        className="my-4",
                        style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4 m-0",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )
        elif confederation == 'CAF':
            CAF= html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                            dbc.Row(
                                dbc.Col(
                                    [
                                        html.Img(src=os.path.join(folder_confe,confederation+".png"), alt="Logo", style={"width": "200px", "height": "150px",'border-radius': '5px'}),
                                        html.Br(),html.Br(),
                                        html.H4("Confederation of African Football"),
                                    ],
                                    className="text-center"
                                )
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[0]), alt="Logo 1", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[1]), alt="Logo 2", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[2]), alt="Logo 3", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[3]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[4]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "90px", "height": "60px"}), width=2, className="text-center p-0")
                                 
                                ],
                                className="mt-4 no-gutters justify-content-center",
                            ),
                        ],
                        className="my-4",
                        style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )
        elif confederation == 'CONCACAF':
            CONCACAF= html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                            dbc.Row(
                                dbc.Col(
                                    [
                                        html.Img(src=os.path.join(folder_confe,confederation+".png"), alt="Logo", style={"width": "200px", "height": "150px",'border-radius': '5px'}),
                                        html.Br(),html.Br(),
                                        html.H4("The Confederation of North, Central America and Caribbean Association Football"),
                                    ],
                                    className="text-center"
                                )
                            ),
                            dbc.Row(
                                [
                                   
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[0]), alt="Logo 1", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[1]), alt="Logo 2", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[2]), alt="Logo 3", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                    dbc.Col(html.Img(src=os.path.join(folder_images,teams_per_confe[3]), alt="Logo 4", className="img-fluid img-thumbnail", style={"width": "85px", "height": "60px"}), width=2, className="text-center p-0"),
                                   
                                ],
                                className="mt-4 no-gutters justify-content-center",
                            ),
                        ],
                        className="my-4",
                        style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )

    return UEFA,CONMEBOL,CONCACAF,AFC,CAF

UEFA,CONMEBOL,CONCACAF,AFC,CAF=imagenes_confe(df_img_team)

confe2=html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                          dbc.Row(
            [
                dbc.Col(
                    [
                        AFC
                    ],
                    width=6
                ),
                dbc.Col(
                    [CAF],
                    width=6
                ),
            ]
        ),],
            className="my-4",
            style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )

confe3=html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                          dbc.Row(
            [
                dbc.Col(
                    [
                        CONMEBOL
                    ],
                    width=6
                ),
                dbc.Col(
                    [CONCACAF],
                    width=6
                ),
            ]
        ),],
            className="my-4",
            style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )

title=dbc.Container([
    dbc.Row([
        html.H2('Football confederations of the world'.upper(),style={'margin':'1vw  0 1vw  0',"text-align":"center"}),
    ])
])

title2=title=dbc.Container([
    dbc.Row([
        html.H2('statistics by confederations'.upper(),style={'margin':'1vw  0 1vw  0',"text-align":"center"}),
    ])
])

#DATASET
df_gra= pd.read_csv('DASHBOARD/assets/datas/dataConfe.csv',sep=',')
grafica1=html.Div([
    html.H4('Average'),
    dcc.Dropdown(
        id="dropdown",
        options=df_gra.columns.to_list()[1:-1],
        value=df_gra.columns.to_list()[1],
      
    ),
    dcc.Graph(id="graph"),
])


@callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def graficaLine(label):
    fig = px.line(df_gra, x="CONFEDERATIONS", y=label)
    fig.update_traces(line = dict(dash = "dot", width = 4, color = "orange"),
                        marker = dict(color = "darkblue", size = 9, opacity = 0.8))
    fig.update_traces(textposition="bottom right")
    fig.update_traces(textposition = "top center")
   
    
    #fig = px.bar(df_gra, x="CONFEDERATIONS", y=label)
    return fig



fig50 = px.bar(df_gra, x="CONFEDERATIONS", y="PERCENT")


grafiProm=html.Div(
            dbc.Container(
                [
                    html.Div(
                        [
                          dbc.Row(
            [
                dbc.Col(
                    [
                        grafica1
                    ],
                    width=6
                ),
                dbc.Col(
                    [
                        html.H4('PERCENT TEAM PER CONFERATIONS'),
                        dcc.Graph(figure=fig50)
                    ],
                    width=6
                ),
            ]
        ),],
            className="my-4",
            style={"text-align": "center"},
                    ),
                ],
                fluid=True,
                className="container mt-4",
                style={"background-color": "#f2f2f2", "padding": "20px","border-radius": "10px"},
            ),
        )



layout = html.Div([
    html.Div(
    [navbar1, navbar2,carousel,title,UEFA,confe3,confe2,title2,grafiProm],style={"background-color": "rgb(235, 231, 231)"})
])

