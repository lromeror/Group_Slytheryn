import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    dbc.Container(
        [
            html.H1("Título", className="text-center"),
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
        ],
        className="d-flex flex-column justify-content-center align-items-center vh-100"
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)