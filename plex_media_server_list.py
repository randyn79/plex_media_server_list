#!/usr/bin/env python3

import os
import pandas as pd
import datetime

def get_files(path) -> dict:
    """Returns a dictionary of the filename, folder, file size, date modified and date accessed."""

    library = {'File':[], 'Folder':[], 'Size (MB)':[], 'Modified':[], 'Accessed':[]}

    for root, dirs, files in os.walk(path):
        for file in files:
            fileroot = os.path.basename(os.path.normpath(root))
            filesize = round(os.path.getsize(os.path.join(root, file)) / 1024 **2, 3)
            modified = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime('%m-%d-%Y')
            accessed = datetime.datetime.fromtimestamp(os.path.getatime(os.path.join(root, file))).strftime('%m-%d-%Y')
            library['Folder'].append(fileroot)
            library['File'].append(file)
            library['Size (MB)'].append(filesize)
            library['Modified'].append(modified)
            library['Accessed'].append(accessed)

    return library


def generate_csv(library):
    """Creates a CSV file of the library dictionary"""
    df = pd.DataFrame(library)
    #df.set_index('File',inplace=True)
    print(df)
    df.to_csv('Media.csv')

path = os.getcwd()
library = get_files(path)
generate_csv(library)
