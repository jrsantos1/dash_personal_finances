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
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, henraça... ", id = 'txt-receita'),
                    
                ], width=6)
            ])
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


