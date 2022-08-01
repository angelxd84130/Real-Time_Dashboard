import pandas as pd
from datetime import datetime
import pymysql
import logging

def db_connect():
    logging.info('connecting to local db..')
    conn = pymysql.connect(host="127.0.0.1", user="root", password='zxcv1234', port=3306)
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



def load_daily_transaction_result(startDate, endDate, sportCodes) -> 'DataFrame':
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_result..')
	sql = """
		SELECT event_date, "success" as result, sum(sum_of_success) as "count"
		FROM EventTracking.sport_transaction_result 
		where (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
		group by event_date 
		union 
		SELECT event_date, "fail" as result, sum(sum_of_fail) as "count" FROM EventTracking.sport_transaction_result 
		where (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
		group by event_date 
		order by event_date 
	"""  % (startDate, endDate, sportCodes, startDate, endDate, sportCodes)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')
	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'result', 'count'])
	return df


def load_daily_transaction_rate(startDate, endDate, sportCodes) -> 'DataFrame':
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_result..')
	sql = """
		SELECT event_date, sum(sum_of_success)/ (sum(sum_of_success) + sum(sum_of_fail))  as "rate"
		FROM EventTracking.sport_transaction_result 
		where (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
		group by event_date 
		
	"""  % (startDate, endDate, sportCodes)
	print(sql)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')
	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'success_rate'])
	return df


def load_daily_transaction_avg(startDate, endDate, sportCodes) -> 'DataFrame':
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_result..')
	sql = """
		SELECT sum(sum_of_success)/ (sum(sum_of_success) + sum(sum_of_fail))  as "success",
		sum(sum_of_fail)/ (sum(sum_of_success) + sum(sum_of_fail))  as "fail"
		FROM EventTracking.sport_transaction_result 
		where (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
	"""  % (startDate, endDate, sportCodes)
	print(sql)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')
	df = pd.DataFrame(cur.fetchall(), index=None, columns=['success', 'fail'])
	return df



def load_daily_transaction_error(startDate, endDate, sportCodes) -> 'DataFrame':
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_error..')
	sql = """
		SELECT event_date, error_code, sum(sum_of_error) 
		FROM EventTracking.sport_transaction_error
		where (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
		group by event_date, error_code 
	"""  % (startDate, endDate, sportCodes)
	print(sql)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')
	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'error_code', 'sum_of_error'])
	df = error_code_mapping(df)
	return df


def load_daily_transaction_error_rate(startDate, endDate, sportCodes) -> 'DataFrame':
	cur, conn = db_connect()
	logging.info('connecting successful. loading data from transaction_error..')
	sql = """
		SELECT * FROM(
			SELECT event_date, error_code, sum(sum_of_error) as "unique_error" 
			FROM EventTracking.sport_transaction_error 
			WHERE (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
			GROUP BY event_date, error_code 
		) A
		LEFT JOIN 
		(SELECT event_date, sum(sum_of_error) as "total_error"  
		FROM EventTracking.sport_transaction_error 
		WHERE (event_date > "%s") and (event_date <= "%s") and sport_code in %s 
		GROUP BY event_date) B on A.event_date=B.event_date
	"""  % (startDate, endDate, sportCodes, startDate, endDate, sportCodes)
	print(sql)
	cur.execute(sql)
	conn.commit()
	logging.info('loading successfully!')
	df = pd.DataFrame(cur.fetchall(), index=None, columns=['event_date', 'error_code', 'unique_error', 'event_date1', 'total_error'])
	df = error_code_mapping(df)
	df['error_rate'] = df['unique_error']/df['total_error']
	return df