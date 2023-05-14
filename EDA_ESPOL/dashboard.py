
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash import Dash, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
df_H_p = pd.read_csv('EDA_ESPOL/data.csv')
width=30
height=30
app = Dash(__name__)
app.layout = html.Div([
    dbc.Card(
    [
        dbc.CardImg(src=f"https://digitalhub.fifa.com/transform/c0ab58e9-0b9c-4f71-9bf4-1e82d77f67e9/1442158606?io=transform:fill,width:{width},height:{height}", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18vw",'margin':'2vw'},),
    dbc.Card(
    [
        dbc.CardImg(src="https://digitalhub.fifa.com/transform/c0ab58e9-0b9c-4f71-9bf4-1e82d77f67e9/1442158606?io=transform:fill,width:30,height:30", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
     style={"width": "18vw",'margin':'2vw'},),
    dbc.Card(
    [
        dbc.CardImg(src="https://digitalhub.fifa.com/transform/c0ab58e9-0b9c-4f71-9bf4-1e82d77f67e9/1442158606?io=transform:fill,width:30,height:30", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18vw",'margin':'2vw'}),
    dbc.Card(
    [
        dbc.CardImg(src="https://digitalhub.fifa.com/transform/c0ab58e9-0b9c-4f71-9bf4-1e82d77f67e9/1442158606?io=transform:fill,width:30,height:30", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18vw",'margin':'2vw'},)
],style={'display':'flex','flex-direction':'row','flex-wrap':'wrap'})


if __name__ == '__main__':
    app.run_server(debug=True)
