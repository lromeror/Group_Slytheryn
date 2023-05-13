
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
from pages import Argentina, Australia,Belgium,Brazil,Canada,Cameroon,Costa_Rica,Croatia, Denmark, Ecuador,England,España,France,Germany,Ghana,Iran,Japan,Korea_Republic,Saudi_Arabic,Marocco,Mexico,Netherlands,Polond,Portugal,Qatar,Senegal,Serbia,Switzerland,Tunisia,Uruguay,United_States,Wales,Confederations,home1

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

list=['Argentina','Australia','Belgium','Brazil','Canada','Cameroon','Costa_Rica','Croatia', 'Denmark', 'Ecuador','England','España','France','Germany','Ghana','Iran','Japan','Korea_Republic','Saudi_Arabic','Marocco','Mexico','Netherlands','Polond','Portugal','Qatar','Senegal','Serbia','Switzerland','Tunisia','Uruguay','United_States','Wales']

@callback(Output('page-content', 'children'),
            Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/Confederations':
        return Confederations.layout
    elif pathname == '/Argentina':
        return Argentina.layout
    elif pathname == '/Australia':
        return Australia.layout
    elif pathname == '/Belgium':
        return Belgium.layout
    elif pathname == '/Brazil':
        return Brazil.layout
    elif pathname == '/Canada':
        return Canada.layout
    elif pathname == '/Cameroon':
        return Cameroon.layout
    elif pathname == '/Costa_Rica':
        return Costa_Rica.layout
    elif pathname == '/Croatia':
        return Croatia.layout
    elif pathname == '/Denmark':
        return Denmark.layout
    elif pathname == '/Ecuador':
        return Ecuador.layout
    elif pathname == '/England':
        return England.layout
    elif pathname == '/España':
        return España.layout
    elif pathname == '/France':
        return France.layout
    elif pathname == '/Germany':
        return Germany.layout
    elif pathname == '/Ghana':
        return Ghana.layout
    elif pathname == '/Iran':
        return Iran.layout
    elif pathname == '/Japan':
        return Japan.layout
    elif pathname == '/Korea_Republic':
        return Korea_Republic.layout
    elif pathname == '/Saudi_Arabic':
        return Saudi_Arabic.layout
    elif pathname == '/Marocco':
        return Marocco.layout
    elif pathname == '/Mexico':
        return Mexico.layout
    elif pathname == '/Netherlands':
        return Netherlands.layout
    elif pathname == '/Polond':
        return Polond.layout
    elif pathname == '/Portugal':
        return Portugal.layout
    elif pathname == '/Qatar':
        return Qatar.layout
    elif pathname == '/Senegal':
        return Senegal.layout
    elif pathname == '/Serbia':
        return Serbia.layout
    elif pathname == '/Switzerland':
        return Switzerland.layout
    elif pathname == '/Tunisia':
        return Tunisia.layout
    elif pathname == '/Uruguay':
        return Uruguay.layout
    elif pathname == '/United_States':
        return United_States.layout
    elif pathname == '/Wales':
        return Wales.layout
    else:
        return home1.layout

if __name__ == '__main__':
    app.run_server(debug=True)