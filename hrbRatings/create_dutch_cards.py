import os
import datetime
import pandas as pd
import numpy as np

pd.options.display.max_columns = 20
pd.options.display.max_rows = 500

'''
	1. Load Daily Report
	1.1 Read dailyreport-<current_date>.csv from csv_downloads_path\\daily_reports to dailyreport dataframe
	1.2 drop unwanted columns
	1.3 sort dataframe by track, time and total
	1.4 extract top 3 totals entries for each time

'''

# set up paths
csv_downloads_path = 'G:\\Dev2022\\projects\\hrb_ratings\\hrbRatings\\csv_downloads\\'
dutch_cards_path = 'G:\\Dev2022\\projects\\hrb_ratings\\hrbRatings\\dutch_cards\\'

# set current_date
current_date = datetime.date.today()

# set up file_names and file_categories lists
file_names = ['cards_','dailyreport-', 'formreport_', 'jockeysreport-', 'LastTenDistances_report_', 
					'OR_report_', 'trainersreport-', 'dutch_card-']
file_categories = ['cards','daily_reports','form_reports','jockey_reports','last10_reports','or_reports','trainer_reports','dutch_cards']

# read dailyreport to dailyreport dataframe (encoding = ISO-8859-1)

# setup columns_to_keep
columns_to_keep = ['time', 'track', 'horse', 'total']

folder = file_categories[1] + '\\'
file_name = file_names[1]
filename =  csv_downloads_path + folder + file_name + str(current_date) + '.csv'

# create dataframe
dailyreport_df = pd.read_csv(filename, encoding='ISO-8859-1')

# drop unwanted columns
dailyreport_df = dailyreport_df[columns_to_keep]

# sort dataframe (by track, time ascending and total descending)
dailyreport_sorted = dailyreport_df.sort_values(by = ['track', 'time', 'total'], axis=0, ascending=[True, True, False], inplace=False,
               kind='quicksort', na_position='first', ignore_index=True, key=None)

# group dataframe with groupby time and track
grouped = dailyreport_sorted.groupby(['time','track'])

dutch_card = pd.DataFrame()
odds = []
# iterate and print top 3 totals in each group
for group, data in grouped:
	top3 = data.nlargest(3, 'total')
	print(f'{top3.track.unique()} : {top3.time.unique()}')
	for i in range(0,3):
		print(f'Enter decimal odds for horse: {top3.iloc[i].horse} : {float(input())}')
	print()
	#dutch_card = pd.concat([dutch_card, top3])
	#print(f'top3[1] = {top3[1]}')
#print(f'dutch_card : {dutch_card}')

# write the dutch card to a csv file
#dutch_folder = file_categories[-1] + '\\'
#dutch_file_name = file_names[-1]
#dutch_filename =  dutch_cards_path + dutch_file_name + str(current_date) + '.csv'

#dutch_card.to_csv(dutch_filename, index=False)

