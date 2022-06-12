import os
import pandas as pd
import numpy as np
from hrbClasses import hrb_classes

def get_load_path(machine):
	if machine == 'desktop':
		load_path = 'G:/Dev2022/projects/hrb_ratings/'
	else:
		load_path = 'C:/Users/bgour/Coding/Dev2022/projects/hrb_ratings/'

	return load_path

def get_daily_report(report_date, machine):
	load_path = get_load_path(machine)
	os.chdir(load_path)

	# data path
	daily_report_path = load_path + 'hrbRatings/csv_downloads/daily_reports/'
	daily_racecards_path = load_path + 'hrbRatings/csv_downloads/cards/'

	daily_report_filename = 'dailyreport-' + report_date + '.csv'
	df_daily_report = pd.read_csv(daily_report_path + daily_report_filename, encoding="ISO-8859-1")

	display_columns = ['race_date', 'track', 'time', 'horse', 'class', 'major','racetype', 
	                   'distance', 'prize', 'going', 'category', 'topor', 'stall', 
	                   'medianOR', 'avgOR', 'code', 'pounds', 'OfficialRating',
	                   'LastRun', 'form', 'stallpos', 'stallsanalyser', 'Career_WinPC', 
	                   'HorseDistanceWin%', 'HorseDistancePlace%', 'HorseTrackWin%', 
	                   'HorseTrackPlace%', 'HorseCDWin%', 'TrkDist_plcPC', 'Class_WinPC', 
	                   'Class_plcPC', 'Going_WinPC', 'Going_plcPC', 'Direction_WinPC', 
	                   'Headgear_WinPC']

	df_horse = df_daily_report[display_columns]

	return df_daily_report, df_horse

def get_last10_report(report_date, machine):
	load_path = get_load_path(machine)
	os.chdir(load_path)

	# data path
	last10_report_path = load_path + 'hrbRatings/csv_downloads/last10_reports/'
	daily_racecards_path = load_path + 'hrbRatings/csv_downloads/cards/'

	last10_report_filename = 'LastTenDistances_report_' + report_date + '.csv'
	df_last10_report = pd.read_csv(last10_report_path + last10_report_filename, encoding="ISO-8859-1")

	# cleanup header fieldnames
	rename_cols_dict = {
		'prevyards' : 'yards1',
		'prevmove' : 'move1',
		'prevrtype' : 'rtype1',
		'prevplacing' : 'placing1',
		'prevrunners' : 'runners1',
		'prevtrack' : 'track1',
		'prevgoing' : 'going1',
		'prevclass' : 'class1'
	}

	df_last10_report.rename(columns = rename_cols_dict, inplace=True)
	# print(df_last10_report.head())

	return df_last10_report

def create_last10_instance(entry, l10_entry):
	for count in range(0,10):
		# l10_instance
		l10_instance = hrb_classes.Last10(entry, count, l10_entry.yards1.item(), l10_entry.move1.item(), 
			l10_entry.rtype1.item(), l10_entry.placing1.item(), l10_entry.runners1.item(), 
			l10_entry.track1.item(), l10_entry.going1.item(), l10_entry.class1.item())
		
		l10_instance.print_last10()
		print()
		
	return l10_instance