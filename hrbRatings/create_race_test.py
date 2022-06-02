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
		# last1
		last1 = hrb_classes.Last10(entry, 1, l10_entry.prevyards.item(), l10_entry.prevmove.item(), 
			l10_entry.prevrtype.item(), l10_entry.prevplacing.item(), l10_entry.prevrunners.item(), 
			l10_entry.prevtrack.item(), l10_entry.prevgoing.item(), l10_entry.prevclass.item())
		l10_entries.append(last1)

		# last2
		last2 = hrb_classes.Last10(entry, 2, l10_entry.yards2.item(), l10_entry.move2.item(), 
			l10_entry.rtype2.item(), l10_entry.placing2.item(), l10_entry.runners2.item(), 
			l10_entry.track2.item(), l10_entry.going2.item(), l10_entry.class2.item())
		l10_entries.append(last2)

		# last3
		last3 = hrb_classes.Last10(entry, 3, l10_entry.yards3.item(), l10_entry.move3.item(), 
			l10_entry.rtype3.item(), l10_entry.placing3.item(), l10_entry.runners3.item(), 
			l10_entry.track3.item(), l10_entry.going3.item(), l10_entry.class3.item())
		l10_entries.append(last3)

	for i in range(0, len(l10_entries)):
		print(l10_entries[i].print_last10())


	race.set_horse_entries(horse_entries)
	race.process_horse_entries()
	race.print_race()
	print()

print(f'Number of races: {len(race_list)}')
