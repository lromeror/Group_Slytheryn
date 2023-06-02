
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from pages import home1,Estadisticas
# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.BOOTSTRAP]  
# external_stylesheets = [dbc.themes.SANDSTONE]
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets,use_pages=True)
server = app.server



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
            Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/Estadisticas':
        return Estadisticas.layout
    else:
        return home1.layout

if __name__ == '__main__':
    app.run_server(debug=True)