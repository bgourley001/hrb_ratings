import os
import glob
import datetime
import shutil

def get_download_date():
	current_date = datetime.date.today()
	# current_date = datetime.date.today() + datetime.timedelta(days=2)

	return current_date

def set_file_paths():
	if os.name == 'nt':  # Windows
		downloads_path = os.path.join('C:/', 'Users/bgour/Downloads/')
		dest_path = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrbRatings/csv_downloads/')
	else:  # Linux or macOS
		downloads_path = os.path.join('/home', 'bill/Downloads/')
		dest_path = os.path.join('/home','bill/development/python_code/hrb_ratings/hrbRatings/csv_downloads/')
	
	#print(f'downloads_path : {downloads_path}')
    
	return downloads_path, dest_path

def copy_to_dest():
	# copy files from Downloads to csv_downloads sub-folders
	downloads_path, dest_path = set_file_paths()
	file_names = ['cards_','dailyreport-', 'formreport_', 'jockeysreport-', 'LastTenDistances_report_', 
			'OR_report_', 'trainersreport-', 'GoingReport_', 'Weight_report_', 'GradeReport_', 'CourseDist_']
	file_categories = ['cards','daily_reports','form_reports','jockey_reports','last10_reports','or_reports','trainer_reports',
		   'going_reports','weight_reports','grade_reports','course_dist_reports']

	count = 0
	for file_category in file_categories:
		folder = f'{file_category}/'
		file_name = file_names[count]
		for name in glob.glob(f'{downloads_path}{file_name}*.*'):
			basename = os.path.basename(name)
			print(f'name : {name}, {basename}')
			shutil.move(f'{name}', f'{dest_path}{folder}{basename}')
			#os.rename(f'{name}', f'{dest_path}{folder}{basename}')
		count += 1

def main():
	downloads_path, dest_path = set_file_paths()

	copy_to_dest()   



# update github
#cmd = 'git add .'
#os.system(cmd)
#cmd = 'git commit -m "Added csv files for "' + str(current_date)
#os.system(cmd)
#cmd = 'git push origin main'
#os.system(cmd)

if __name__ == "__main__":
      main()
      

