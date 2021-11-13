import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)


def layout():
    df = pd.read_csv('/data/data.csv')
    fig = px.line(df, x="Time", y="Power Level", color='Cat', title='Cat Power level Evolution')

    return html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(id='example-graph', figure=fig)
    ])

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')