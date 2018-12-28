import pandas as pd
import numpy as np
import glob
import sys
import os
from pandas import ExcelWriter


'''worked to merge all lld files into one excel. take out that first row in xls so can go into 
merge_vl.py immediately and also maybe try to combine both ot those into lld_collect_xls.py. 
also adjust output xls file name to something that works for everyone'''

def main():
    writer = pd.ExcelWriter('lld_merge_output_all_second.xlsx')

    all_lld_data = pd.DataFrame()
    script = sys.argv[0]
    lld_files = sys.argv[1:] #../../downloads/pg_ttd_logs*.csv

    for i in lld_files:
            string_version_lld_file = str(i)
            df = pd.read_csv(string_version_lld_file, header=None, engine='python')
            all_lld_data = all_lld_data.append(df, ignore_index=True)

    all_lld_data.to_excel(writer, 'Sheet1')
    writer.save()


if __name__ == "__main__":
    main()


'''Make your code publish-read:

Create a python package:

To create a package, create a folder that is named exactly how you want your package to be named. Place all the files and classes that you want to ship into this folder.

Now, create a file called __init__.py (again two underscores). Open the file with your text editor of choice. In this file, you write nothing but import statements that have the following schema:

Create the files PyPi needs:


setup.py
setup.cfg
LICENSE.txt
README.md (optinal but highly recommended)
'''

