import os
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

drive_letter = 'G:'
load_path = drive_letter + '/Dev2022/projects/hrb_ratings/'
os.chdir(load_path)

# data path
daily_report_path = load_path + 'hrb_ratings/csv_downloads/daily_reports/'
daily_racecards_path = load_path + 'hrb_ratings/csv_downloads/cards/'

report_date = '2022-05-07'

def add_race_class_to_daily_report(df_daily_report, race_class_list):
	if df_daily_report['class'] == 'Irish':
		if df_daily_report.major == 'Non-Major':
			if df_daily_report.prize < 5000:
				race_class = 'Class 6'
			elif df_daily_report.prize < 7000:
				race_class = 'Class 5'
			elif df_daily_report.prize < 10000:
				race_class = 'Class 4'
			elif df_daily_report.prize < 14000:
				race_class = 'Class 3'
			else:
		 		race_class = 'Class 2'
		else:
			if major == 'Group 3':
		 		race_class = 'Group 3'
			elif major == 'Group 2':
		 		race_class = 'Group 2'
			elif major == 'Group 1':
		 		race_class = 'Group 1'
			else:
		 		# Listed Race
		 		race_class = 'class 1'
		race_class_list.append(race_class)
	else:
		df_daily_report['race_class'] = df_daily_report['class']
	return df_daily_report

def align_daily_report_and_racecards(df_daily_racecards, df_daily_report):
	# compare card output with daily report output
	horse_list_1 = df_daily_report.horse
	horse_list_2 = df_daily_racecards.Horse
	horse_diff = list(set(horse_list_2) - set(horse_list_1))

	# remove rows from racecard where horse is in horse_diff
	for horse in horse_diff:
		df_daily_racecards.drop(df_daily_racecards[df_daily_racecards.Horse == horse].index, inplace=True)

	return df_daily_racecards

def get_daily_racecards(daily_racecards_path, report_date):
	daily_racecards_filename = 'cards_' + report_date + '.csv'
	df_daily_racecards = pd.read_csv(daily_racecards_path + daily_racecards_filename, encoding="ISO-8859-1")
	print(df_daily_racecards.shape)
	
	cols = df_daily_racecards.columns

	print('daily racecards columns...\n')
	print(*cols, sep = ", ")

	display_columns = ['Date', 'RaceTime', 'Track', 'RaceName', 'Distance', 'Dist_Furlongs', 'Class','Going', 
	                   'PrizeMoney', 'Runners', 'Direction', 'CardNo', 'Horse', 'HorseAge', 
	                   'Jockey', 'JClaim', 'Trainer', 'Stall', 'OfficialRating',
	                   'Weight_Pounds', 'Odds', 'Form', 'Days', 'Headgear', 
	                   'Stallion', 'Dam', 'HorseType', 
	                   'CD', 'numfences']

	print('\nCreating racecards dataframe...')
	df_racecards = df_daily_racecards[display_columns]
	print(df_racecards.head())

	classes = df_daily_racecards.Class.unique()
	print(*classes, sep = ", ")

	return df_racecards


def get_daily_report(daily_report_path, report_date):
	daily_report_filename = 'dailyreport-' + report_date + '.csv'
	df_daily_report = pd.read_csv(daily_report_path + daily_report_filename, encoding="ISO-8859-1")
	print(df_daily_report.shape)

	cols = df_daily_report.columns

	print('daily report columns...\n')
	print(*cols, sep = ", ")

	display_columns = ['race_date', 'track', 'time', 'horse', 'class', 'major','racetype', 
	                   'distance', 'prize', 'going', 'category', 'topor', 'stall', 
	                   'medianOR', 'avgOR', 'code', 'pounds', 'OfficialRating',
	                   'LastRun', 'form', 'stallpos', 'stallsanalyser', 'Career_WinPC', 
	                   'HorseDistanceWin%', 'HorseDistancePlace%', 'HorseTrackWin%', 
	                   'HorseTrackPlace%', 'HorseCDWin%', 'TrkDist_plcPC', 'Class_WinPC', 
	                   'Class_plcPC', 'Going_WinPC', 'Going_plcPC', 'Direction_WinPC', 
	                   'Headgear_WinPC']

	print('\nCreating horse dataframe...')
	df_horse = df_daily_report[display_columns]

	report_classes = df_horse['class'].unique()
	print(*report_classes, sep = ", ")

	print(df_horse.head())

	return df_daily_report, df_horse

def get_class_score(df):
	# 'Class 6' 'Class 5' 'Irish' 'Class 3' 'Class 2' 'Class 4' 'Class 1'
	return



# rating settings dictionaries
class_scores = {
	'Class 7' : 80,
	'Class 6' : 85,
	'Class 5' : 90,
	'Class 4' : 95,
	'Class 3' : 100,
	'Class 2' : 105,
	'Class 1' : 110,
	'Group 3' : 115,
	'Group 2' : 120,
	'Group 1' : 125
	
}

# load reports
# create dataframes
print('Load daily report...')
df_daily_report, df_horse = get_daily_report(daily_report_path, report_date)

print('Load daily racecards...')
df_daily_racecards = get_daily_racecards(daily_racecards_path, report_date)

print('Aligning daily_racecards and daily_report')
df_daily_racecards = align_daily_report_and_racecards(df_daily_racecards, df_daily_report)
print(df_daily_racecards.shape)
print(df_daily_report.shape)

# df_daily_racecards_groupby_min = df_daily_racecards.groupby(['Class'], as_index=False)[['PrizeMoney']].min()
# print(df_daily_racecards_groupby_min)
# df_daily_racecards_groupby_max = df_daily_racecards.groupby(['Class'], as_index=False)[['PrizeMoney']].max()
# print(df_daily_racecards_groupby_max)
# print()
# df_horse_groupby_min = df_horse.groupby(['class'], as_index=False)[['prize']].min()
# print(df_horse_groupby_min)
# df_horse_groupby_max = df_horse.groupby(['class'], as_index=False)[['prize']].max()
# print(df_horse_groupby_max)

# add race_class variable to the daily report calculated from Irish and UK classes
race_class_list = []
df_daily_report['race_class'] = add_race_class_to_daily_report(df_daily_report, race_class_list)
