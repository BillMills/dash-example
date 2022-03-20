import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

def strip(text):
    try:
        t = text.strip().strip('"').strip("'")
        return t
    except AttributeError:
        return text

def stripnum(text):
    if text is '':
        return float('NaN')
    try:
        t = text.strip('\s\"\'')
        if t[-1] == 'k':
            return float(t[0:-1])*1000
        if t[-1] == 'µ':
            return float(t[0:-1])/1000000
        return float(t)

    except AttributeError:
        return text

def layout():
    df = pd.read_csv('/data/data.csv', sep=",", converters={0: strip, 1: strip, 2: stripnum})  
    df['Date']= pd.to_datetime(df['Date'], format= '%Y-%m-%dT%H:%M:%S.%f+00:00')
    print(df.columns[0])
    fig = px.line(df, x=df.columns[1], y=df.columns[2], color=df.columns[0], title=df.columns[1] + ' vs ' + df.columns[2] + ' per ' + df.columns[0])
    return html.Div(children=[
        html.H1(children='Classes @ NYC Resistor'),

        dcc.Graph(id='example-graph', figure=fig)
    ])

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
