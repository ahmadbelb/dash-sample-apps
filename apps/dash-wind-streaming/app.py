
from db.api import getdata

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly

import plotly.graph_objs as go
from collections import deque
import pandas as pd

X = deque(maxlen = 200)
X.append(1)

Y = deque(maxlen = 200)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
	[
		dcc.Graph(id = 'live-graph', animate = True
                  ,),
		dcc.Interval(
			id = 'graph-update',
			interval = 15000,
			n_intervals = 0,
		),
	]
)

@app.callback(
	Output('live-graph', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_scatter(n):

    xa= getdata()
    print(xa)

    timera=xa[xa['variable_name'] == 'act-hose-diameter-1']['timestamp']
    # rti=(xa[xa['variable_name'] == 'act-hose-diameter-1']['timestamp'].values.astype(np.int64) // 10 ** 9)
    X=pd.to_datetime(timera, unit='ms').dt.tz_localize('UTC').dt.tz_convert('Europe/Paris')
    print(pd.date_range(start=X.min(),end=X.max()))
    Y=(xa[xa['variable_name'] == 'act-hose-diameter-1']['value'])

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers',
            marker_color = "#FFFFFF"

    ,



    )
    return {'data': [data],
			'layout' : go.Layout(yaxis_color="#FFFFFF",xaxis_color="#FFFFFF",plot_bgcolor=app_color["graph_bg"],
            paper_bgcolor=app_color["graph_bg"] ),
            }

if __name__ == '__main__':
	app.run_server(threaded=True,host='0.0.0.0')
