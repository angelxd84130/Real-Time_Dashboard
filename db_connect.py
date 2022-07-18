import pandas as pd
from datetime import datetime
import pymysql
import logging

def db_connect():
    logging.info('connecting to local db..')
    conn = pymysql.connect(host="127.0.0.1", user="root", password='zxcv1234', port=3306, db='BetSlip')
    cur = conn.cursor()
    logging.info('connect success!')
    return cur, conn


def error_code_mapping(df):
	code_dic = [
		['101',  ':赔率检查比数错误(多原因)'],
		['304',  ':超过单场赔付上限'],
		['5001', ':赔率或盘口已变更'],
		['501',  ':下注金额超过用户余额'],
		['6001', ':注单金额低于最小投注金额'],
		['7002', ':用户登入错误'],
		['8001', ':XML 格式错误'],
		['9001', ':下注行为程序的错误'],
		['null', ':(APP/mobile未知错误)'],
		['1000', ':数据库连接错误'],
		['2001', ':10秒内重复下注'],
		['0',    ':找不到账户余额信息'],
		['2002', ':用户未登入'],
		['900', ':数据库查询余额时产生错误'],
		['赔率或盘口已变更', ''],
		['系统忙碌中，请稍后再试。', '']
	]

	code_dic = pd.DataFrame(code_dic, columns=['code', 'map_name'])
	df = df.merge(code_dic, how='left', left_on=['error_code'], right_on=['code'])
	#df = df.fillna('')
	df['error_name'] = df['error_code'] + df['map_name']
	print(df)
	return df

    

def load_transaction_success_rate(startDate, endDate):
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_success_rate..')
	sql = """
		Select * From EventTracking.transaction_success_rate 
    	where (event_date > "%s") and (event_date <= "%s") ; 
    	""" % (startDate, endDate)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')

	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'sum_of_success', 'sum_of_fail', 'success_rate'])
	df['total_transactions'] = df['sum_of_success'] + df['sum_of_fail']
	return df





def load_transaction_error_count(startDate, endDate):
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_error_count..')
	sql = """
		Select * From EventTracking.transaction_error_count 
    	where (event_date > "%s") and (event_date <= "%s") ; 
    	""" % (startDate, endDate)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')

	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'error_code', 'sum_of_error', 'error_rate'])
	df = error_code_mapping(df)
	return df




