import os
import pandas as pd
import numpy as np
from tabulate import tabulate

from hrbClasses import hrb_classes, utility

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

machine = 'desktop'
# machine = 'laptop'

report_date = '2022-05-25'

# load reports for report_date
# create race and horse classes for report date
print('Load daily report...')
df_daily_report, df_horse = utility.get_daily_report(report_date, machine)

print('Load Last10 Distance Report...')
df_last10 = utility.get_last10_report(report_date, machine)

# create race entry list
df_grouped = df_daily_report.groupby('time').nth(0).reset_index()

race_list = []
for count in range(0, len(df_grouped)):
	entry = df_grouped.iloc[count]
	# create Race entry
	today_race = hrb_classes.Race(entry.race_date, entry.track, entry.time, 
		entry.race_name, entry['class'], entry.race_restrictions, entry.major, entry.racetype, 
		entry.distance, entry.prize, entry.going, entry.runners, entry.category, entry.direction,
		entry.topor)

	race_list.append(today_race)

for race in race_list:
	# add horse entries
	entries = df_horse.loc[(df_horse.race_date == race.get_race_date()) & 
	(df_horse.track == race.get_track()) & (df_horse.time == race.get_time())].horse
	horse_entries = []
	l10_entries = []

	for entry in entries:
		horse_form = df_horse.loc[(df_horse.horse == entry)].form.item()
		horse_entry = hrb_classes.Horse(entry, horse_form)
		horse_entries.append(horse_entry)

		l10_entry = df_last10.loc[(df_last10.horse_name == entry)]

		l10_entries.append(utility.create_last10_instance(entry, l10_entry))

	race.set_horse_entries(horse_entries)
	race.process_horse_entries()
	race.print_race()
	print()

print(f'Number of races: {len(race_list)}')
