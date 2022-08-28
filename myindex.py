from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import sidebar, dashboards, extratos

from app import *

# =========  Layout  =========== #
content = html.Div(id="page-content")

# Layout principal do aplicativo ---- dbc container utilizado para dividir o layout em colunas em linhas

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        
        dbc.Col([
            content
        ], md = 10),
    ])

], fluid=True,)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    if pathname == '/extratos':
        return extratos.layout


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)