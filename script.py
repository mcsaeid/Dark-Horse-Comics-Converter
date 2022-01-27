import os
import json
import tarfile
import zipfile
import shutil
import requests
import time
from googlesearch import search
import bs4

print('This script will convert your Dark Horse comics to a CBZ format.\n')

while True:
    print('-'*25)
    tar_path = input('Enter the path of the tar file: ')
    folder_path = os.path.dirname(tar_path)
    new_path = fr"{folder_path}\book"

    #Extracting the tar file

    print('\nExtracting the tar file . . .')
    file1 = tarfile.open(tar_path)
    file1.extractall(new_path)

    file1.close()
    print('Done!\n')

    #Renaming the files to JPG in the correct order

    print('Converting the files to JPG . . .')

    file = open(fr"{new_path}\manifest.json",)
    data = json.load(file)
    uuid = data["book_uuid"]

    for i in data['pages']:
        page_number = i["sort_order"]
        page_name = i["src_image"]
        os.rename(fr"{new_path}\{page_name}",fr"{new_path}\{page_number}.jpg")

    file.close()
    print('Done!\n')

    #Zipping the JPGs into a CBZ

    print('Zipping the JPGs into a CBZ . . .')

    zipped_file = zipfile.ZipFile(fr'{folder_path}\book.cbz','w')

    for folder_name, subfolders, file_names in os.walk(fr"{new_path}\\"):
        for file_name in file_names:
            file_complete = folder_name + file_name 

            if 'jpg' in file_complete:
                timestamp = time.mktime((1980, 1, 1, 0, 0, 0, 0, 0, 0))
                os.utime(file_complete, (timestamp, timestamp))
                zipped_file.write(file_complete, arcname = file_name)

    zipped_file.close()
    print('Done!\n')

    print('Removing the temporary files...')       
    shutil.rmtree(new_path)
    print('Done!\n')

    #Getting the book title

    print('Getting the book title from Google . . .')
    try:
        for url in search(uuid, num_results=3):
            if "darkhorse" in url:
                lorl = url

    except Exception:
        print('\nUnable to get the book title using the following UUID:', uuid, '\nTry googling the ID inside quotation marks: “Example.” Then, rename the CBZ file manually.\n\nOperation completed.\n')

    ff = requests.get(lorl)
    ffx = bs4.BeautifulSoup(ff.text, 'html.parser')
    str1 = ffx.title.text
    str2 = str1.split('|')
    str3 = str2[0].strip('\n ')
    str3 = str3.replace(':', '-')
    os.rename(fr'{folder_path}\book.cbz', fr'{folder_path}\{str3}.cbz')

    print('Done!\n')
    print('\nOperation completed.\n')
