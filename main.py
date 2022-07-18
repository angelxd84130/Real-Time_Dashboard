import dash
from dash import dcc
from dash import html
import plotly_express as px
import plotly.graph_objs as go
import db_connect as db
from datetime import datetime, timedelta  
from dash.dependencies import Input, Output


''' auto refreash '''
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



def get_time(val: str):
	if val == 'days7':
		startTime = (datetime.now() + timedelta(days=-7)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')
	elif val == 'days14':
		startTime = (datetime.now() + timedelta(days=-14)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')
	elif val == 'days30':
		startTime = (datetime.now() + timedelta(days=-30)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')
	elif val == 'days60':
		startTime = (datetime.now() + timedelta(days=-60)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')
	elif val == 'days90':
		startTime = (datetime.now() + timedelta(days=-90)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')	
	elif val == 'days120':
		startTime = (datetime.now() + timedelta(days=-120)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')	
	else: 
		startTime = (datetime.now() + timedelta(days=-365)).strftime('%Y-%m-%d')
		endTime = datetime.now().strftime('%Y-%m-%d')


	return startTime, endTime


''' load data '''
startTime, endTime = get_time('days7')

def get_data(startTime, endTime):

	transaction_success_rate = db.load_transaction_success_rate(startTime, endTime) 
	transaction_eror = db.load_transaction_error_count(startTime, endTime) 
	return transaction_success_rate, transaction_eror



''' make figs '''
transaction_success_rate, transaction_eror = get_data(startTime, endTime)

def get_pic1(transaction_success_rate):
	pic1 = px.line(transaction_success_rate, x='event_date', y='success_rate', height=500, width=1100)
	pic1.update_layout(
		title="交易送出成功比例",
		title_font_size=20,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=15),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=20)),
		xaxis=dict(titlefont=dict(size=20)),
		margin_t=50, margin_b=200)
	return pic1


def get_pic2(transaction_success_rate):
	pic2 = px.line(transaction_success_rate, x='event_date', y='total_transactions', height=500, width=1100)
	pic2.update_layout(
		title="交易送出次数",
		title_font_size=20,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=15),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=20)),
		xaxis=dict(titlefont=dict(size=20)),
		margin_t=50, margin_b=120)
	return pic2


def get_fig1(transaction_eror):
	fig1 = px.line(transaction_eror, x='event_date', y='sum_of_error', color='error_name', height=500, width=1200)
	fig1.update_layout(
		title="交易失败原因总数量",
		title_font_size=20,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=15),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=20)),
		xaxis=dict(titlefont=dict(size=20)),
		margin_t=50, margin_b=120)
	return fig1

def get_fig2(transaction_eror):
	fig2 = px.line(transaction_eror, x='event_date', y='error_rate', color='error_name', height=500, width=1200)
	fig2.update_layout(
		title="交易失败原因分布",
		title_font_size=20,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=15),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=20)),
		xaxis=dict(titlefont=dict(size=20)),
		margin_t=50, margin_b=120)
	return fig2

pic1 = get_pic1(transaction_success_rate)
pic2 = get_pic2(transaction_success_rate)
fig1 = get_fig1(transaction_eror)
fig2 = get_fig2(transaction_eror)

pic1.update_traces(mode='lines+markers')
pic2.update_traces(mode='lines+markers')
fig1.update_traces(mode='lines+markers')
fig2.update_traces(mode='lines+markers')

app = dash.Dash()
app.title = "transaction retular report"
app.layout = html.Div(
	[
	html.Div('埋点数据'),
	html.H2('Load data in..'),
	html.Div(dcc.Dropdown(id='dropdown', 
		options=[
		{'label':'past 7 days', 'value':'days7'}, 
		{'label':'past 14 days', 'value':'days14'}, 
		{'label': 'past 30 days', 'value':'days30'}, 
		{'label': 'past 60 days', 'value':'days60'}, 
		{'label': 'past 90 days', 'value':'days90'}, 
		{'label': 'past 120 days', 'value':'days120'},
		{'label': 'past 1 year', 'value':'year1'},
		])),
	html.H2(''),
	dcc.Graph(id='pic2', figure=pic2),
	dcc.Graph(id='pic1', figure=pic1),
	dcc.Graph(id='fig1', figure=fig1),
	dcc.Graph(id='fig2', figure=fig2)]
	)


''' dropdown '''
@app.callback(Output('pic1', 'figure'), Input('dropdown', 'value'))
def update_graph(value):
	startTime, endTime = get_time(value)
	transaction_success_rate, transaction_eror = get_data(startTime, endTime)
	pic1 = get_pic1(transaction_success_rate)
	return pic1


@app.callback(Output('pic2', 'figure'), Input('dropdown', 'value'))
def update_graph(value):
	startTime, endTime = get_time(value)
	transaction_success_rate, transaction_eror = get_data(startTime, endTime)
	pic2 = get_pic2(transaction_success_rate)
	return pic2


@app.callback(Output('fig1', 'figure'), Input('dropdown', 'value'))
def update_graph(value):
	startTime, endTime = get_time(value)
	transaction_success_rate, transaction_eror = get_data(startTime, endTime)
	fig1 = get_fig1(transaction_eror)
	return fig1



@app.callback(Output('fig2', 'figure'), Input('dropdown', 'value'))
def update_graph(value):
	startTime, endTime = get_time(value)
	transaction_success_rate, transaction_eror = get_data(startTime, endTime)
	fig2 = get_fig2(transaction_eror)
	return fig2


if __name__ == '__main__':
	app.run_server(debug=True, host='0.0.0.0')
