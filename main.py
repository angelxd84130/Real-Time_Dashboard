from dash import dcc, html, Dash
import plotly.graph_objs as go
import db_connect as db
from dash.dependencies import Input, Output
import parse as p
import layouts as l


''' auto refreash '''
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)



''' load data '''
def get_data(startTime, endTime, sports):
	daily_transaction_rate = db.load_daily_transaction_rate(startTime, endTime, sports) 
	transaction_error = db.load_daily_transaction_error(startTime, endTime, sports) 
	transaction_error_rate = db.load_daily_transaction_error_rate(startTime, endTime, sports)
	transaction_avg = p.get_transaction_avg(db.load_daily_transaction_avg(startTime, endTime, sports))
	daily_transaction_result = db.load_daily_transaction_result(startTime, endTime, sports)
	return daily_transaction_result, daily_transaction_rate, transaction_error, transaction_error_rate, transaction_avg



''' make figs '''
def make_figs(past_date='days7', sports=['00001']):
	startTime, endTime = p.get_time(past_date)
	sports = p.sport_code_process(sports)
	daily_transaction_result, daily_transaction_rate, transaction_error, transaction_error_rate, transaction_avg = get_data(startTime, endTime, sports)
	pic1 = l.get_pic1(daily_transaction_rate)
	pic2 = l.get_pic2(daily_transaction_result)
	fig1 = l.get_fig1(transaction_error)
	fig2 = l.get_fig2(transaction_error_rate)
	pie1 = l.get_pie1(transaction_avg)
	return pic1, pic2, fig1, fig2, pie1


pic1, pic2, fig1, fig2, pie1 = make_figs()
pic1.update_traces(mode='lines+markers')
fig1.update_traces(mode='lines+markers')
fig2.update_traces(mode='lines+markers')
pie1.update_traces(textposition='inside', textinfo='percent+label')


''' website '''
app = Dash()
app.title = "transaction retular report"
fsize = 15
fcolor = 'MediumTurqoise'
lstyle = style={'color':fcolor, 'font-size':fsize, 'margin':'2px 4px', 'padding-rigth':'20'}

app.layout = html.Div(
	id="app-container",
	children=[
		html.Div(
			id="app-content",
			children=[
				
				html.Div(
					id="top",
					children=[
						html.H1(['埋点数据'], style={'width':'10%'}),
						dcc.Dropdown(
							id='dropdown', 
							options=[
								{'label':'past 7 days', 'value':'days7'}, 
								{'label':'past 14 days', 'value':'days14'}, 
								{'label': 'past 30 days', 'value':'days30'}, 
								{'label': 'past 60 days', 'value':'days60'}, 
								{'label': 'past 90 days', 'value':'days90'}, 
								{'label': 'past 120 days', 'value':'days120'},
								{'label': 'past 1 year', 'value':'year1'},
							],
							placeholder='select',
							value='days7',
							style={'width': '40%', 'margin':'12px 10px'}
						),
						dcc.Checklist(
							id='checklist',
							options=[
								{'label': html.Div(['00: 全部'], lstyle), 'value': '00000'},
								{'label': html.Div(['01: 足球'], lstyle), 'value': '00001'},
								{'label': html.Div(['02: 篮球'], lstyle), 'value': '00002'},
								{'label': html.Div(['03: 棒球'], lstyle), 'value': '00003'},
								{'label': html.Div(['04: 冰上曲棍球'], lstyle), 'value': '00004'},
								{'label': html.Div(['05: 网球'], lstyle), 'value': '00005'},
								{'label': html.Div(['06: 手球'], lstyle), 'value': '00006'},
								{'label': html.Div(['12: 英式橄榄球'], lstyle), 'value': '00012'},
								{'label': html.Div(['16: 橄榄球'], lstyle), 'value': '00016'},
								{'label': html.Div(['20: 乒乓球'], lstyle), 'value': '00020'},
								{'label': html.Div(['21: 板球'], lstyle), 'value': '00021'},
								{'label': html.Div(['22: 飞镖'], lstyle), 'value': '00022'},
								{'label': html.Div(['23: 排球'], lstyle), 'value': '00023'},
								{'label': html.Div(['29: 五人制足球'], lstyle), 'value': '00029'},
								{'label': html.Div(['31: 羽毛球'], lstyle), 'value': '00031'},
								{'label': html.Div(['34: 沙滩排球'], lstyle), 'value': '00034'},
								{'label': html.Div(['111: 电竞'], lstyle), 'value': '00111'},

							],
							value=['00001'],
							inline=True,
							style={'width':'40%', }
						),
					],
					
					style={'padding':'0', 'width':'100%', 'max-width':'100%', 'height':'100%', 'display':'flex', 
					'flex-direction':'row', 'justify-content':'center', 'margin':'0'}
				),
				html.H2(''),
				html.Div(
					id="status-container",
					children=[
						# leftside
						html.Div(
							id="quick-stats",
							children=[
								html.Div(
									id="transaction_avg",
									children=[
										dcc.Graph(id='pie1', figure=pie1)
									]),
								html.H3('world'),
							],
							style={'display':'flex', 'flex-direction':'column', 'align-items':'center', 'justify-content:':'flex-start',
							'flex':'11', 'padding':'1rem', 'max-width':'25%', 'height':'15rem'}
						),

						# rightside
						html.Div(
							id="graphs_container",
							children=[
								html.Div(
									id="transaction_rate",
									children=[
										html.Div("Transaction"),
										html.Div(
											children=[
												html.Div(
													children=[
														dcc.Graph(id='pic2', figure=pic2),
													],
												),
												html.Div(
													children=[
														dcc.Graph(id='pic1', figure=pic1),
													],
												),

											],
											style={'overflow-y':'scroll', 'width':'80.2%', 'height':'24rem',}
										)	
									],
									style={'height':'100%', 'flex': '11 auto'},
									
								),
								html.Div(
									id="error_rate",
									children=[
										html.Div("Error Code"),
										html.Div(
											children=[
												html.Div(
													children=[
														dcc.Graph(id='fig1', figure=fig1),
													],
												),
												html.Div(
													children=[
														dcc.Graph(id='fig2', figure=fig2),
													],
												),
											],
											style={'overflow-y':'scroll', 'width':'80.2%', 'height':'24rem',}
										)							
									],
									style={'height':'100%', 'flex': '11 auto'},
								),
								
							],
							style={'width':'100%', 'display': 'flex', 'flex-direction': 'column', 'flex':'31', 'max-width':'calc(75%)'}
						)

					],
					style={'padding':'0', 'width':'100%', 'max-width':'100%', 'height':'100%', 'display':'flex', 
					'flex-direction':'row', 'justify-content':'center', 'margin':'0'}
				),
				
			],
			style={'background':'inherit', 'padding':'0', 'width':'100%', 'max-width':'100%'}
		)
	],
	style={'background':'#CCFFFF',  'max-width':'100%', 'width':'100%', 'height':'calc(100vh - 1rem)', 'padding':'0'},
	
)



''' dropdown & checkbox update '''
@app.callback([
	Output('pic1', 'figure'),
	Output('pic2', 'figure'),
	Output('fig1', 'figure'), 
	Output('fig2', 'figure'),
	Output('pie1', 'figure')
	], [Input('dropdown', 'value'), Input('checklist', 'value')])

def update_graph(past_date, sports):
	return make_figs(past_date, sports)



if __name__ == '__main__':
	app.run_server(debug=True, host='0.0.0.0')
