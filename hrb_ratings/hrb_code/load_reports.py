import os
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

machine = 'desktop'
# machine = 'laptop'

if machine == 'desktop':
	load_path = 'G:/Dev2022/projects/hrb_ratings/'
else:
	load_path = 'C:/Users/bgour/Coding/Dev2022/projects/hrb_ratings/'

os.chdir(load_path)

# data path
daily_report_path = load_path + 'hrb_ratings/csv_downloads/daily_reports/'
daily_racecards_path = load_path + 'hrb_ratings/csv_downloads/cards/'

report_date = '2022-05-07'

# class_score mapping
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

# score multiplier mapping
score_multipliers = {
	'race_value_multiplier' : 1,
	'top_or_multiplier' : 1,
	'prior_win' : 1,
	'prior_place' : 1
}

def get_finish(form, position):
	finish = form[position]

	return finish

def get_no_of_places(runners):
	if runners < 5:
		places = 1
	elif runners < 8:
		places = 2
	elif runners < 16:
		places = 3
	else:
		places = 4

	return places

def add_race_class(df):
	race_class_list = []
	for race_index in df.index:
		class_entry = df.loc[race_index,'class']
		major = df.loc[race_index,'major']
		prize = df.loc[race_index,'prize']

		# print(f"{race_index}, {track}, {time}, {horse}, class_entry : {class_entry}, major : {major}, prize : {prize}")
		race_class_list.append(get_race_class(class_entry, major, prize))

	df['race_class'] = race_class_list

	return df

def get_race_class(class_entry, major, prize):
	if class_entry == 'Irish':
		if major == 'Non-Major':
			if prize < 5000:
				race_class = 'Class 6'
			elif prize < 7000:
				race_class = 'Class 5'
			elif prize < 10000:
				race_class = 'Class 4'
			elif prize < 14000:
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
	else:
		race_class = class_entry

	return race_class

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

def get_prior_form_score(lr_finish, places, score_multipliers):
	score = 0
	if lr_finish <= places:
		if lr_finish > 1:
			score = score_multipliers.get('prior_place')
		elif lr_finish == 1:
			score = score_multipliers.get('prior_win')

	return score

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

def add_rating_scores(df, class_scores, score_multipliers):
	# race class
	df = add_race_class(df)
	df['race_class_score'] = df.race_class.map(class_scores)

	# race_value
	df = df.assign(rounded_prize = lambda x: (x.prize/1000).round(0).astype(int))
	# adjust rounded_prize to <= max_rounded_prize
	df.rounded_prize = df.apply(lambda x: x.rounded_prize if x.rounded_prize <= 20 else 20, axis=1)
	df['race_value_score'] = df.rounded_prize * score_multipliers.get('race_value_multiplier')

	# top OR
	df['top_or_score'] = df.topor * score_multipliers.get('top_or_multiplier')

	# prior form
	position = -1
	df['lr_finish'] = df['form'].apply(lambda x: get_finish(x, position))
	# convert lr_finish to an integer
	df['lr_finish'] = pd.to_numeric(df['lr_finish'], errors='coerce')
	df['number_of_places'] = df['runners'].apply(lambda x: get_no_of_places(x))
	df['prior_form_score'] = df.apply(lambda x: get_prior_form_score(x['lr_finish'], x['number_of_places'], score_multipliers), axis=1)

	# race score
	race_score_columns = ['race_class_score', 'race_value_score', 'top_or_score', 'prior_form_score']
	df['race_score'] = df[race_score_columns].sum(axis=1)

	return df

# load reports
# create dataframes
print('Load daily report...')
df_daily_report, df_horse = get_daily_report(daily_report_path, report_date)

print('Load daily racecards...')
df_daily_racecards = get_daily_racecards(daily_racecards_path, report_date)

# remove Unnamed column from daily_report
df_daily_report.drop('Unnamed: 183', axis=1, inplace=True)

# align racecards and daily report
print('Aligning daily_racecards and daily_report')
df_daily_racecards = align_daily_report_and_racecards(df_daily_racecards, df_daily_report)
print(df_daily_racecards.shape)
print(df_daily_report.shape)

# add rating scores to daily report
df_daily_report = add_rating_scores(df_daily_report, class_scores, score_multipliers)

# test prints
cols_to_print = ['race_class_score', 'race_value_score', 'top_or_score', 'prior_form_score', 'race_score']

print(df_daily_report[cols_to_print].head(20))