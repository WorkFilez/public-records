# Import Libraries
import pandas as pd
import os
import shutil
import re


# Reads file, converts it to a dataframe, removes PII, writes CSV
def read_edit_file():
    # Read file
    data = pd.read_excel("Open Data Public Records Requests.xlsx", sheet_name=None)
    # Make dataframe
    df = pd.DataFrame(data['Public Records Requests'])
    # Remove new line character, street addresses, and email addresses (in that order)
    df = df.replace(r'\n',' ', regex=True)
    df = df.replace(r'(\d{1,10}( \w+){1,10}( ( \w+){1,10})?( \w+){1,10}[,.](( \w+){1,10}(,)? [A-Z]{2}( [0-9]{5})?)?)', 'REDACTED', regex=True)
    df = df.replace(r'[[\w\.-]+@[\w\.-]+(\.[\w]+)+', 'REDACTED', regex=True)
    # writes CSV
    df.to_csv('public-records-cleaned.csv')
    # Call function to move file
    move_file()

def move_file():
    # SRC Path/DEST path (fill in on OD server)
    source = ""
    destination = ""
    # Does the actual moving
    shutil.move(source, destination)

# Begin script
read_edit_file()