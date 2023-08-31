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

def convert_date_format(filename):
    if 'results_' in filename:
        date_str = filename.split('_')[1].split('.')[0]
        parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        new_filename = filename.replace(date_str, formatted_date)
        return new_filename
    
    return filename

def handle_filenames(downloads_path, dest_path, file_category, file_name, files_to_rename):
    folder = f'{file_category}/'
    for name in glob.glob(f'{downloads_path}{file_name}*.*'):
        filename = os.path.basename(name)

        if filename in files_to_rename:
            new_filename = f'{downloads_path}{file_name}_{get_download_date()}.xlsx'
            shutil.move(name, new_filename)
            filename = new_filename

        new_filename = convert_date_format(filename)
        shutil.move(name, f'{dest_path}{folder}{new_filename}')
        print(f'{name} moved from downloads to {dest_path}{folder}{new_filename}')
  
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
		file_name = file_names[count]
		handle_filenames(downloads_path, dest_path, file_category, file_name, files_to_rename)
		count += 1

def main():
	downloads_path, dest_path = set_file_paths()

	copy_to_dest()   

if __name__ == "__main__":
      main()
      

