import os
import pandas as pd
import datetime

# 1. set file paths
def set_file_paths():
	if os.name == 'nt':  # Windows
		downloads_path = os.path.join('C:/', 'Users/bgour/Downloads/')
		dest_path = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrbRatings/csv_downloads/')
		results_path = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrbRatings/csv_downloads/results/')
	else:  # Linux or macOS
		downloads_path = os.path.join('/home', 'bill/Downloads/')
		dest_path = os.path.join('/home','bill/development/python_code/hrb_ratings/hrbRatings/csv_downloads/')
		results_path = os.path.join('/home','bill/development/python_code/hrb_ratings/hrbRatings/csv_downloads/results')
	
	return downloads_path, dest_path, results_path

# 2. set result start date
def set_result_dates(result_start_date, result_end_date):
	start_date = result_start_date
	end_date = result_end_date

	return start_date, end_date

# 3. read file csv files into a datafile
def read_csv_file(filename):
	df = pd.read_csv(filename)

	return df

# 4. create filenames to load
def create_filenames(results_path, start_date, end_date):
	filenames = []
	for d in [start_date, end_date]:
		filename = os.path.join(results_path, f'results_{start_date}.csv')
		print(f'filename = {filename}')
		filenames.append(filename)
		
	return filenames

def main():
    downloads_path, dest_path, results_path = set_file_paths()
    print(f'downloads_path = {downloads_path}\ndest_path = {dest_path}\nresults_path = {results_path}')

    start_date, end_date = set_result_dates('2013-1-1', '2013-1-2')

    print(f'start_date = {start_date}, end_date = {end_date}')

    filenames = create_filenames(results_path, start_date, end_date)

    print(f'filenames = {filenames}')
	
if __name__ == "__main__":
	main()