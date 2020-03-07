import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import matplotlib.dates as md
from xlsxwriter.utility import xl_rowcol_to_cell
import matplotlib.ticker as ticker
import seaborn as sns
import calendar
from pandas.tseries.offsets import MonthEnd
from numbers import Number
import a_functions as a_fun
import math

#new to change widthÎ
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)


comp = pd.read_excel('ComplaintsExport2020-03-06.xlsx',header=1)

comp_date = ['Date','Date of Manufacture','Durability Date']

def date_cleaner(df,cols):
    '''
    Cleans dates in files

    '''
    for col in cols:
        df[col] = pd.to_datetime(df[col], format="%d %b %Y")
    return df

date_cleaner(comp,comp_date)

print('ehl')
