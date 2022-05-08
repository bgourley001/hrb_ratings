import os
import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

drive_letter = 'G:'
load_path = drive_letter + '/Dev2022/projects/hrb_ratings/'
os.chdir(load_path)

# data path
daily_report_path = load_path + 'hrb_ratings/csv_downloads/daily_reports/'

daily_report_date = '2022-05-07'
daily_report_filename = 'dailyreport-' + daily_report_date + '.csv'

def get_class_score(df):
	# 'Class 6' 'Class 5' 'Irish' 'Class 3' 'Class 2' 'Class 4' 'Class 1'
	return

# load daily report
# create dataframe
print('    Creating daily report dataframe...')
df_daily_report = pd.read_csv(daily_report_path + daily_report_filename, encoding="ISO-8859-1")
# print(df_daily_report.shape)

cols = df_daily_report.columns
for col in cols:
	print(col)

# print(df_daily_report.head(5))

display_columns = ['race_date', 'track', 'time', 'horse', 'class', 'major','racetype', 
                   'distance', 'prize', 'going', 'category', 'topor', 'stall', 
                   'medianOR', 'avgOR', 'code', 'pounds', 'OfficialRating',
                   'LastRun', 'form', 'stallpos', 'stallsanalyser', 'Career_WinPC', 
                   'HorseDistanceWin%', 'HorseDistancePlace%', 'HorseTrackWin%', 
                   'HorseTrackPlace%', 'HorseCDWin%', 'TrkDist_plcPC', 'Class_WinPC', 
                   'Class_plcPC', 'Going_WinPC', 'Going_plcPC', 'Direction_WinPC', 
                   'Headgear_WinPC']

df_horse = df_daily_report[display_columns]
print(df_horse.shape)
# print(df_horse)
print(df_horse['class'].unique())

#print(tabulate(df_horse.head(5), headers='keys', tablefmt='psql'))

df_horse_groupby = df_horse.groupby(['race_date', 'track', 'time'], as_index=False)['horse','class', 'major','prize']
print(df_horse_groupby.first())

#df_horse_groupby.to_html('temp2.html')