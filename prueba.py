import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('Restaurant tips by day of week'),
    dcc.Dropdown(
        id="dropdown20",
        options=[{"label": day, "value": day} for day in ["Fri", "Sat", "Sun"]],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph50"),
])

@app.callback(
    Output("graph50", "figure"), 
    Input("dropdown20", "value"))
def update_bar_chart(day):
    df = px.data.tips() # reemplaza esto con tu propia fuente de datos
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
