import dash 
import dash_bootstrap_components as dbc
from dash import dcc
from layout import conteudo
from layout_novo import conteudo as new_content

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.BOOTSTRAP]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

app.layout = dbc.Container([
   new_content
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
