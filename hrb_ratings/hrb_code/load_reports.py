import os
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# machine = 'desktop'
machine = 'laptop'

if machine == 'desktop':
	load_path = 'G:/Dev2022/projects/hrb_ratings/'
else:
	load_path = 'C:/Users/bgour/Coding/Dev2022/projects/hrb_ratings/'

os.chdir(load_path)

# data path
daily_report_path = load_path + 'csv_downloads/daily_reports/'
daily_racecards_path = load_path + 'csv_downloads/cards/'

report_date = '2022-05-09'

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

	#display_columns = ['race_date', 'track', 'time', 'horse', 'class', 'major','racetype', 
	#                   'distance', 'prize', 'going', 'category', 'topor', 'stall', 
	#                   'medianOR', 'avgOR', 'code', 'pounds', 'OfficialRating',
	#                   'LastRun', 'form', 'stallpos', 'stallsanalyser', 'Career_WinPC', 
	#                   'HorseDistanceWin%', 'HorseDistancePlace%', 'HorseTrackWin%', 
	#                   'HorseTrackPlace%', 'HorseCDWin%', 'TrkDist_plcPC', 'Class_WinPC', 
	#                   'Class_plcPC', 'Going_WinPC', 'Going_plcPC', 'Direction_WinPC', 
	#                   'Headgear_WinPC']

	print(df_daily_racecards.head())

	return df_daily_racecards


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

	print(df_horse.head())

	return df_daily_report, df_horse

def get_class_score(df):
	# 'Class 6' 'Class 5' 'Irish' 'Class 3' 'Class 2' 'Class 4' 'Class 1'
	return

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

#df_horse_groupby = df_horse.groupby(['race_date', 'track', 'time'], as_index=False)[['horse','class', 'major','prize']]
#print(df_horse_groupby.first().head())

