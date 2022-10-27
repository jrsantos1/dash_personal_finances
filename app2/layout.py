from datetime import date
import string
from turtle import width
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
import pandas as pd
from collections import OrderedDict

# layout

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

table_teste = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}
)
## abstrair
def card_info(id: string, size: int, info: string, value: string):
  return dbc.Col([
            dbc.Row([
                html.Div([
                    html.H5(info),
                    html.H5(value, className="text-primary", style={"margin-left": "10px"})], style={"display": "flex"}, id=id)
                ],)]
    ,width=size)

def flex_items(title, element2, size):
    return dbc.Col([html.Div([
        html.H5(title),
        element2
    ], style={"display": "flex"})], width=size)


risco_metricas = dbc.Container([
     dbc.Row([
        card_info(value="0.00", info="Patrimônio (em milhões)", id="sas", size=3),
        card_info(value="0.00", info="VaR (1du IC) (em milhões)", id="asas", size=3),
        card_info(value="0.00", info="VaR %PL", id="asasasa", size=3),
        card_info(value="0.00", info="Vol Ex-ante %PL", id="a", size=3)
    ], className="mt-5 d-flex")
    ], fluid=True)

tabs_controle_item_childen = dbc.Container([
      dbc.Row([
                dbc.Col([html.H5("Controle:"),dcc.Dropdown(id="sml_controle_select", 
                             options=[
                                  {"label": "Option 1", "value": 1},
                                  {"label": "Option 2", "value": 2},
                                 ])], width=3),
                dbc.Col([html.H5("Métodologia:"),dcc.Dropdown(id="sml_controle_metodologia_select", 
                             options=[
                                  {"label": "Option 1", "value": 1},
                                  {"label": "Option 2", "value": 2},
                                 ])], width=3),
                dbc.Col([html.H5("IC Controle(%):"), dbc.Input(type="text", placeholder="IC Controle(%)")], width=2),
                dbc.Col([html.H5("Limite %PL:"), dbc.Input(type="text", placeholder="Limite %PL")], width=2),
                dbc.Col([html.H5("HP (DU):"), dbc.Input(type="text", placeholder="HP (DU)")], width=2),
     ], className="mt-5"),
      
      dbc.Row([
                dbc.Col([html.H5("Classe:"),dcc.Dropdown(id="sml_controle_classe", 
                             options=[
                                  {"label": "Option 1", "value": 1},
                                  {"label": "Option 2", "value": 2},
                                 ])], width=3),
                dbc.Col([html.H5("Peso:"),dcc.Dropdown(id="sml_controle_peso", 
                             options=[
                                  {"label": "Option 1", "value": 1},
                                  {"label": "Option 2", "value": 2},
                                 ])], width=3),
                dbc.Col([html.H5("Benchmark:"), dbc.Input(type="text", placeholder="Benchmark")], width=2),
                dbc.Col([html.Div(className="fa fa-plus mt-5"),html.Div(className="fa fa-trash", style={"margin-left":"5px"})], width=1)
               
      ], className="mt-5"),
      dbc.Row([
          dbc.Col([dbc.Button("Consultar", color='secondary', outline=True)])
      ], className="mt-5")
      
    ],fluid=True)

tabs_controle_item_resultado = dbc.Container([
    dbc.Row([
        card_info(value="0.00", info="Métrica", id="sml_controle_resultado_metrica", size=3),
        card_info(value="0.00", info="Utilização", id="sml_controle_resultado_utilizacao", size=3)
    ], className="mt-5")
], fluid=True)

tabs_controle_group = dbc.Tabs([
                dbc.Tab(dbc.Container(tabs_controle_item_childen,fluid=True), label="Param controles"),
                dbc.Tab(tabs_controle_item_resultado, label="Resultado"),
                dbc.Tab("Con,teudo Parametros de Controle", label="Param controles"),
            ]),

tabs_workflow_item = dbc.Container([dbc.Col([
    dbc.Row([
        html.Div([
            html.H5("Simulação ID"),
            html.H5("0", style={"margin-left": "10px"}, className="text-primary")
        ], className="d-flex")
    ], className="mt-2"),
    dbc.Row([
        dbc.Col([
            dbc.Progress(value=50)
        ], width=12)
    ], className="mt-4")
    
])], fluid=True, className="mt-5")

# layout

conteudo = dbc.Col([
    
            html.H1("Simulação de Risco", className="mt-3"),
 #Linha de inputs para consulta
            dbc.Row([
                dbc.Col([dbc.Input(type="date")], width=3),
                dbc.Col([dbc.Select(required=True, options=[
                    {'label': 'Fundo1'},
                    {'label': 'Fundo2'}
                    ], value="teste")]),
                dbc.Col(dbc.Button("Consultar", color='secondary', outline=True)),
            ], className="mt-5"),
            dbc.Row([
                card_info(value="0.00", info="Patrimônio (em milhões)", id="sml_patrimonio", size=3),
                card_info(value="0.00", info="VaR (1du IC) (em milhões)", id="sml_var_em_milhoes", size=3),
                card_info(value="0.00", info="VaR %PL", id="sml_var_percentual_pl", size=3),
                card_info(value="0.00", info="Vol Ex-ante %PL", id="vol_ex_ante", size=3),
            ], className="mt-5 d-flex"),
            
# tabs dados controles 
            dbc.Row([
                dbc.Tabs([
                    dbc.Tab(html.H1("Conteudo Exposição"), label="Exposição"),
                    dbc.Tab(tabs_controle_group, label="Dados Controle"),
                    dbc.Tab(html.H1(tabs_workflow_item), label="WorkFlow"),
                    dbc.Tab(risco_metricas, label="Riscos Métrica"),
                ])
            ], className="mt-5")  
            ], className="mt-5")
        

