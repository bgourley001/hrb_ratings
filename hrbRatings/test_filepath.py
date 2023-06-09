import os

def set_file_path(filepath):
    if os.name == 'nt':  # Windows
        file_path = os.path.join('G:\\', filepath)
    else:  # Linux or macOS
        file_path = os.path.join('/', 'path', 'to', filename)

    return file_path

#downloads_path = 'C:\\Users\\bgour\\Downloads\\'
#dest_path = 'G:\\Dev2022\\projects\\hrb_ratings\\hrbRatings\\csv_downloads\\'

filename = 'cards_2022-05-03.csv'
filepath = 'Dev2022\projects\hrb_ratings\hrbRatings\csv_downloads\cards\\'
file_path = set_file_path(filepath)

filename = f'{file_path}{filename}'
print(f'filename : {filename}')