from datetime import datetime, timedelta  
import pandas as pd
import plotly_express as px

''' data process '''

# time process
def get_time(val: str):
	if val == 'days7':
		n = 7
	elif val == 'days14':
		n = 14
	elif val == 'days30':
		n = 30
	elif val == 'days60':
		n = 60
	elif val == 'days90':
		n = 90	
	elif val == 'days120':
		n = 120
	elif val == 'year1':
		n = 365
	else: 
		n = 7

	startTime = (datetime.now() + timedelta(days=-n)).strftime('%Y-%m-%d')
	endTime = datetime.now().strftime('%Y-%m-%d')
	return startTime, endTime


# transaction-avg process
def get_transaction_avg(df):
	print(df)
	if df['success'] is None or df['fail'] is None:
		df = [[0, 'success'],[0, 'fail']]
	else:
		success = sum(df['success'])
		fail = sum(df['fail'])
		df = [[success, 'success'],[fail, 'fail']]
		
	df = pd.DataFrame(df, columns=['sum', 'result'])
	return df


# sport code process
def sport_code_process(sport_codes: list) -> str:
	
	if len(sport_codes) == 0:
		return '(00000)'
	if '00000' in sport_codes:
		return "('00001', '00002', '00003', '00004', '00005', '00006', '00007', '00012', '00013', '00016', '00020', '00021', '00022', '00023', '00026', '00029', '00031', '00034', '00111')"
	if len(sport_codes) == 1:
		return '(' + sport_codes[0] + ')'
	return str(tuple(sport_codes))
