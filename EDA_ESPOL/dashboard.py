
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash import Dash, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd

df_H_p = pd.read_csv('data.csv')
app = Dash(__name__)

app.layout = html.Div([
    html.H1('MATERIAS DISPONIBLES POR FACULTAD'),
    dcc.Dropdown(df_H_p.UNIDAD.unique(), 'Facultad de Ciencias Naturales y Matemáticas', id='dropdown-selection'),
    dcc.Dropdown(df_H_p.UNIDAD.unique(), 'Facultad de Ciencias Naturales y Matemáticas', id='dropdown-selection'),
    dcc.Graph(id='graph-facultad'),
    html.Button('Click here to see the content', id='show-secret'),
    dcc.Graph(id='graph-horarios')
])
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                    size="pop", color="continent", hover_name="country",
                    log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
