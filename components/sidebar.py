import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Meu Orçamento", className="text-primary"),
    html.P("Por Jhonatan Ribeiro", className="text-info"),
    html.Hr(),
        
    # Seção Perfil ----------------
    dbc.Button(id='botao_avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                         ], style = {'background-color' : 'transparent', 'border-color' : 'transparent'}),
    
    # Seção Novo ----------------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id = 'open-novo-receita',
                       children=['+ Receita'])
        ], width = 6),
        dbc.Col([
            dbc.Button(color='danger', id = 'open-novo-despesa',
                       children=['+ Despesa'])
        ], width = 6)

    ]),

    # Modal receita------------------
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
        dbc.ModalBody([
            # --------- Formulário
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, henraça... ", id = 'txt-receita'),
                    
                ], width=6),
                
                dbc.Col([
                    dbc.Label('Valor: '),
                    dbc.Input(placeholder="Ex.: $100.00 ", id = 'valor-receita'),
                    
                ], width=6)
            ]),
            
            # ---------- Calendário
            
            dbc.Row([
                dbc.Col([
                    dbc.Label('Data: '),
                    dcc.DatePickerSingle(id = 'data-receitas',
                                         min_date_allowed=date(2020,1,1,),
                                         max_date_allowed=date(2030,12,31),
                                         date=datetime.today(),
                                         style={'width' : '100%'})
                ], width=4),
                
                dbc.Col([
                    dbc.Label("Extras:"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-receita',
                        switch=True
                    )
                ]),
                
                dbc.Col([
                    html.Label('Categoria receita'),
                    dbc.Select(id='select_receita', options=[], value=[])
                ], width=4)                
            ],  style={'margin-top': '25px'}),
            
            dbc.Row(
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend('Adicionar Categoria', style={'color': 'green'}),
                                dbc.Input(type='text', placeholder='Nova categoria... ', id='input-add-receita', value=''),
                                html.Br(),
                                dbc.Button('Adicionar', className='btn btn-sucess', id='add-category-receita', style={'margin-top': '20px'}),
                                html.Br(),
                                html.Div(id='category-div-add-receita', style={})
                            ])
                        ])
                    ])
                ]), style={'margin-top': '20px'}
            )
            
            
        ])
    ], id = 'modal_novo_receita'),

    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
        dbc.ModalBody([])
    ],id = 'modal_novo_despesa'),

    # Seção NAV ----------------------------------
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extratos", active="exact"),
    ], style={"margin-bottom": "50px"}, vertical=True, pills=True, id="nav_buttons")

], style={"border": "2px blue solid", "padding": "0px", "margin": "0px"}, id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal_novo_despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal_novo_despesa', 'is_open')

)
def open_modal(input, state):
    if input:
        return not state


@app.callback(
    Output('modal_novo_receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal_novo_receita', 'is_open')

)
def open_modal(input, state):
    if input:
        return not state


