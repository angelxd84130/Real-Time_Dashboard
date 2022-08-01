from datetime import datetime, timedelta  
import pandas as pd
import plotly_express as px



''' pic contents & layouts '''

height = 400
axis = 15
title_font_size = 17
font = 12

def get_pic1(transaction_success_rate):
	pic1 = px.line(transaction_success_rate, x='event_date', y='success_rate', height=height)
	pic1.update_layout(
		title="交易送出成功比例",
		title_font_size=title_font_size,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=font),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=axis)),
		xaxis=dict(titlefont=dict(size=axis)),
		margin_t=50, margin_b=0)
	return pic1


def get_pic2(daily_transaction_result):
	#pic2 = px.line(daily_transaction_result, x='event_date', y='total_transactions', height=height, width=width)
	pic2 = px.bar(daily_transaction_result, x="event_date", y="count", color="result")		
	pic2.update_layout(
		title="交易送出次数",
		title_font_size=title_font_size,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=font),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=axis)),
		xaxis=dict(titlefont=dict(size=axis)),
		margin_t=50, margin_b=120)
	return pic2


def get_fig1(transaction_eror):
	fig1 = px.line(transaction_eror, x='event_date', y='sum_of_error', color='error_name', height=height)
	fig1.update_layout(
		title="交易失败原因总数量",
		title_font_size=title_font_size,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=font),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=axis)),
		xaxis=dict(titlefont=dict(size=axis)),
		margin_t=50, margin_b=120)
	return fig1

def get_fig2(transaction_eror):
	fig2 = px.line(transaction_eror, x='event_date', y='error_rate', color='error_name', height=height)
	fig2.update_layout(
		title="交易失败原因分布",
		title_font_size=title_font_size,
		hoverlabel_font=dict(size=15, color='black'),
		font=dict(size=font),
		legend_font=dict(size=15),
		yaxis=dict(titlefont=dict(size=axis)),
		xaxis=dict(titlefont=dict(size=axis)),
		margin_t=50, margin_b=0)
	return fig2

def get_pie1(transaction_avg):
	pie1 = px.pie(transaction_avg, values='sum', names='result', height=370, width=400, 
		color_discrete_map={'sum_of_success':'royalred', 'sum_of_fail':'royalblue'})
	pie1.update_layout(
		title="Avg of success_rate",
		title_font_size=title_font_size,
		hoverlabel_font=dict(size=10, color='black'),
		font=dict(size=font),
		yaxis=dict(titlefont=dict(size=20)),
		xaxis=dict(titlefont=dict(size=20)),
		)
	return pie1
