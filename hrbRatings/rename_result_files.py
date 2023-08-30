import os
import shutil
from datetime import datetime

def convert_date_format(old_date_str):
    parsed_date = datetime.strptime(old_date_str, '%Y-%m-%d')
    new_date_str = parsed_date.strftime('%Y-%m-%d')
    return new_date_str

def parse_result_files(source_folder, dest_folder):
    for filename in os.listdir(source_folder):
        if filename.startswith('results_') and filename.endswith('.csv'):
            parts = filename.split('_')
            if len(parts) == 3:
                old_date_str = parts[1].split('.')[0]
                new_date_str = convert_date_format(old_date_str)
                new_filename = f'results_{new_date_str}.csv'
                source_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(dest_folder, new_filename)
                shutil.copy(source_path, dest_path)
                print(f'Converted: {source_path} => {dest_path}')

source_folder = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrb_ratings/hrbRatings/csv_downloads/results/')
dest_folder = os.path.join('G:/', 'Dev2022/projects/hrb_ratings/hrb_ratings/hrbRatings/csv_downloads/results/new/')

parse_result_files(source_folder, dest_folder)