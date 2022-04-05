import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import requests
import json

# Initialize the app
app = dash.Dash(suppress_callback_exceptions=True)
with open('../coin_api_key.json') as file:
    apikey = json.load(file).get('key')
server = app.server

app.title = 'Africa Data School Crypto App'
app.description = "This is a test app for Africa Data School Jan 2022 Cohort"

app.layout = html.Div(children=[
    html.Link(rel='shortcut icon', type='favicon.ico', href='assets/btc.png'),
    html.Div([
        # Logo Div
        html.Div([
            # image
            html.Img(src=app.get_asset_url('btc.png'), id='ads-image', style={
                'height': '60px',
                'width': 'auto',
                'margin-bottom': '25px'
            })

        ], className='one-third column'),

        # Adds heading   DIV
        html.Div([
            # heading
            html.Div([
                html.H2('Africa Data School ', style={'margin-bottom': '0px', 'color': 'pink'}),
                html.H5('Cryptocurrency Prices', style={'margin-bottom': '0px', 'color': 'pink'})
            ])

        ], className='one-third column', id='title'),
        # date
        html.Div([], className='one-third column', id='title1')

    ], id='header', className='row flex-display', style={'margin-bottom': '25px'}),
    # DROPDOWN SECTION

    # Select crypto
    html.Div([
        html.Div([
            html.Label('Crypto Asset', style={'color': '#FF00BD'}),
            dcc.Dropdown(
                id='coin',
                options=[
                    {'label': 'Bitcoin', 'value': 'BTC'},
                    {'label': 'Ethereum', 'value': 'ETH'},
                    {'label': 'Bitcoin Cash', 'value': 'BCH'},
                    {'label': 'Litecoin', 'value': 'LTC'}
                ],
                value='BTC'
            ),

        ], className='card_container three columns'),

        # Select Time Period
        html.Div([
            html.Label('Time', style={'color': '#FF00BD'}),
            dcc.Dropdown(
                id='time',
                options=[
                    {'label': 'Minute', 'value': '1MIN'},
                    {'label': 'Day', 'value': '10DAY'},
                    {'label': 'Month', 'value': '6MTH'},
                    {'label': 'year', 'value': '5YRS'}
                ],
                value='10DAY'
            ),

            dcc.Interval(
                id='graph-update',
                interval=1 * 10,
                n_intervals=1
            ),

        ], className='card_container three columns'),
    ], className='row flex display'),

    # DISPLAY PRICE OPENING, PRICE CLOSING, PRICE HIGH and VOLUME TRADE.

    # Price Opening
    html.Div([
        html.Div([
            html.H6(children='Price Open',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(id='price_open',
                   style={'textAlign': 'center',
                          'color': 'orange',
                          'fontSize': 40}),

        ], className='card_container three columns'),

        # Price Closing
        html.Div([
            html.H6(children='Price Close',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(id='price_close',
                   style={'textAlign': 'center',
                          'color': 'orange',
                          'fontSize': 40}),

        ], className='card_container three columns'),

        # Price high
        html.Div([
            html.H6(children='Price High',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(id='price_high',
                   style={'textAlign': 'center',
                          'color': 'orange',
                          'fontSize': 40}),

        ], className='card_container three columns'),

        # Volume Traded
        html.Div([
            html.H6(children='Volume Traded',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(id='Volume_traded',
                   style={'textAlign': 'center',
                          'color': 'orange',
                          'fontSize': 40}),

        ], className='card_container three columns')

    ], className='row flex display'),
    # THE GRAPH
    html.Div([
        html.Div([
            dcc.Graph(id='graph', config={'displayModeBar': False}),
        ], className='card_container twelve columns')
    ], className='row flex display'),
], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})



if __name__ == "__main__":
    app.run_server(debug=True)