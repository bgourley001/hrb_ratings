import os
import datetime

# set up paths
downloads_path = 'C:\\Users\\bgour\\Downloads\\'
dest_path = 'G:\\Dev2022\\projects\\hrb_ratings\\hrbRatings\\csv_downloads\\'

current_date = datetime.date.today()
# current_date = datetime.date.today() + datetime.timedelta(days=2)

# copy files from Downloads to csv_downloads sub-folders
file_names = ['cards_','dailyreport-', 'formreport_', 'jockeysreport-', 'LastTenDistances_report_', 
					'OR_report_', 'trainersreport-', 'GoingReport_', 'Weight_report_']
file_categories = ['cards','daily_reports','form_reports','jockey_reports','last10_reports','or_reports','trainer_reports','going_reports','weight_reports']

count = 0
for file_category in file_categories:
	folder = file_category + '\\'
	file_name = file_names[count]

	filename =  downloads_path + file_name + str(current_date) + '*'

	cmd = 'move ' + filename + ' ' + dest_path + folder
	print('cmd = ' + cmd)
	os.system(cmd)
	count += 1

# update github
cmd = 'git add .'
os.system(cmd)
cmd = 'git commit -m "Added csv files for "' + str(current_date)
os.system(cmd)
cmd = 'git push origin main'
os.system(cmd)

