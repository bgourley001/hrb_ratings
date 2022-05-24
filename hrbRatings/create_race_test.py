import os
import pandas as pd
import numpy as np
from tabulate import tabulate

from hrbClasses import hrb_classes

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
daily_report_path = load_path + 'hrbRatings/csv_downloads/daily_reports/'
daily_racecards_path = load_path + 'hrbRatings/csv_downloads/cards/'

report_date = '2022-05-07'

def get_daily_report(daily_report_path, report_date):
	daily_report_filename = 'dailyreport-' + report_date + '.csv'
	df_daily_report = pd.read_csv(daily_report_path + daily_report_filename, encoding="ISO-8859-1")
	print(df_daily_report.shape)

	cols = df_daily_report.columns

	# print('daily report columns...\n')
	# print(*cols, sep = ", ")

	display_columns = ['race_date', 'track', 'time', 'horse', 'class', 'major','racetype', 
	                   'distance', 'prize', 'going', 'category', 'topor', 'stall', 
	                   'medianOR', 'avgOR', 'code', 'pounds', 'OfficialRating',
	                   'LastRun', 'form', 'stallpos', 'stallsanalyser', 'Career_WinPC', 
	                   'HorseDistanceWin%', 'HorseDistancePlace%', 'HorseTrackWin%', 
	                   'HorseTrackPlace%', 'HorseCDWin%', 'TrkDist_plcPC', 'Class_WinPC', 
	                   'Class_plcPC', 'Going_WinPC', 'Going_plcPC', 'Direction_WinPC', 
	                   'Headgear_WinPC']

	# print('\nCreating horse dataframe...')
	df_horse = df_daily_report[display_columns]

	report_classes = df_horse['class'].unique()
	# print(*report_classes, sep = ", ")

	# print(df_horse.head())

	return df_daily_report, df_horse

# load reports
# create dataframes
print('Load daily report...')
df_daily_report, df_horse = get_daily_report(daily_report_path, report_date)

# create race entry list
df_grouped = df_daily_report.groupby('time').nth(0).reset_index()

race_list = []
for count in range(0, len(df_grouped)):
	entry = df_grouped.iloc[count]

	# create Race entry
	race = hrb_classes.Race(entry.race_date, entry.track, entry.time, 
		entry.race_name, entry['class'], entry.race_restrictions, entry.major, entry.racetype, 
		entry.distance, entry.prize, entry.going, entry.runners, entry.category, entry.direction,
		entry.topor)

	race_list.append(race)

for race in race_list:
	# add horse entries
	entries = df_horse.loc[(df_horse.race_date == race.get_race_date()) & 
	(df_horse.track == race.get_track()) & (df_horse.time == race.get_time())].horse
	horse_entries = []
	for entry in entries:
		horse_form = df_horse.loc[(df_horse.horse == entry)].form.item()
		horse_entry = hrb_classes.Horse(entry, horse_form)
		horse_entries.append(horse_entry)

	race.set_horse_entries(horse_entries)
	race.process_horse_entries()
	race.print_race()
	print()

print(f'Number of races: {len(race_list)}')
