import pandas as pd
import numpy as np
import glob
import sys
import os
from pandas import ExcelWriter
'''currently this merges a bunch of lld files into on pandas data frame, ttd_lld.py will
aim to then print it into an excel sheet. merge_vl.py is able to merge on common header name
so ttd impression id for the test.'''

#/Users/taylorhiggins/downloads
# from tah ../../downloads/pg_ttd_logs*.csv
#hardcoded way worked 
# def main():
#     all_data = pd.DataFrame()
#     for f in glob.glob("../tah/pg_ttd_logs*.csv"):
#         #print(f) #string of file name
#         df = pd.read_csv(f)
#         all_data = all_data.append(df, ignore_index=True)
#         print(all_data)

# if __name__ == "__main__":
#     main()

def main():
    all_data = pd.DataFrame()
    script = sys.argv[0] #name of this py file
    ttd_file = sys.argv[1] #MOAT_Test_Imp IDs.xlsx
    lld_files = sys.argv[2:] #../tah/pg_ttd_logs*.csv #../../downloads/pg_ttd_logs*.csv
    for i in lld_files:
        string_version_lld_file = str(i)
        df = pd.read_csv(string_version_lld_file, header=None, engine='python')
        all_data = all_data.append(df, ignore_index=True)

    return all_data

# def merge_on_impression_ID():
#     df1 = all_data
#     df2 = pd.read_excel(ttd_file) #turn ttd into dataframe
#     results = df1.merge(df2, on = 'TTD_IMPRESSIONID')
#     print(results)
#     return results
    #make this function work like merge_vl.py


if __name__ == "__main__":
    main()
  




