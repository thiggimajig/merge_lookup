import pandas as pd 
import numpy as np
from pandas import ExcelWriter
#import sys

'''worked to do vlookup on ttd and moat impression level data and print out matches.
next add in sys options for column merged on and files read excel from. and adjust naming 
output xlsx file for something that works for everyone maybe based off of read excel file name
or in moat py'''

def main():
    writer = pd.ExcelWriter('vlookup_all_lld_files_bid_id.xlsx')

    df1 = pd.read_excel('bid_id_lld_merge_output_all_ttd.xlsx', sheet_name = 'MOAT', encoding="utf-8")
   
    df2 = pd.read_excel('bid_id_lld_merge_output_all_ttd.xlsx', sheet_name = 'TTD', encoding="utf-8")
    
    results = pd.merge(df1, df2, on ='ID', how = 'inner')

    results.to_excel(writer, 'Sheet1')
    writer.save()

if __name__ == "__main__":
    main()


'''Make your code publish-read:

Create a python package:

To create a package, create a folder that is named exactly how you want your package to be named. Place all the files and classes that you want to ship into this folder.
folder = merge_lookup in

Now, create a file called __init__.py (again two underscores). Open the file with your text editor of choice. In this file, you write nothing but import statements that have the following schema:

Create the files PyPi needs:

setup.py
setup.cfg
LICENSE.txt
README.md (optinal but highly recommended)
'''