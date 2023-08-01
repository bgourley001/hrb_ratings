import os
import glob
import datetime
import shutil

def get_download_date():
	download_date = datetime.date.today()

	return download_date

def set_file_paths():
	if os.name == 'nt':  # Windows
		downloads_path = os.path.join('C:/', 'Users/bgour/Downloads/')
		dest_path = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrb_ratings/hrbRatings/csv_downloads/')
	else:  # Linux or macOS
		downloads_path = os.path.join('/home', 'bill/Downloads/')
		dest_path = os.path.join('/home','bill/development/python_code/hrb_ratings/hrbRatings/csv_downloads/')

	return downloads_path, dest_path

def copy_to_dest():
	# copy files from Downloads to csv_downloads sub-folders
	downloads_path, dest_path = set_file_paths()
	file_names = ['cards','dailyreport', 'formreport', 'jockeysreport', 'LastTenDistances_report', 
			'OR_report', 'trainersreport', 'GoingReport', 'Weight_report_', 'GradeReport', 
			'CourseDist', 'results']
	file_categories = ['cards','daily_reports','form_reports','jockey_reports','last10_reports',
		    'or_reports','trainer_reports','going_reports','weight_reports','grade_reports',
			'course_dist','results']

	count = 0
	files_to_rename = ['CourseDistToday.xlsx', 'GoingReportToday.xlsx', 'GradeReportToday.xlsx']
	for file_category in file_categories:
		folder = f'{file_category}/'
		file_name = file_names[count]
		for name in glob.glob(f'{downloads_path}{file_name}*.*'):
			filename = os.path.basename(name)
			if filename in files_to_rename:
				shutil.move(f'{name}', f'{downloads_path}{file_name}_{get_download_date()}.xlsx')
				name = f'{downloads_path}{file_name}_{get_download_date()}.xlsx'
			basename = os.path.basename(name)
			print(f'name : {name}, {basename}')
			shutil.move(f'{name}', f'{dest_path}{folder}{basename}')
		count += 1

def main():
	downloads_path, dest_path = set_file_paths()

	copy_to_dest()   

if __name__ == "__main__":
      main()
      

