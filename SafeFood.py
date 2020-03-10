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


def date_cleaner(df,cols):
    '''
    Cleans dates in files

    '''
    for col in cols:
        df[col] = pd.to_datetime(df[col], format="%d %b %Y")
    return df

def ffill(df, cols):
    '''
    forward fill for corrective actions
    '''
    for col in cols:
        df[col] = df[col].ffill()
    return df

'''
This is for Complaints Export last 12 months 
'''
# comp = pd.read_excel('ComplaintsExport 2020-03-09.xlsx',header=1)
# comp_date = ['Date','Date of Manufacture','Durability Date']
# date_cleaner(comp,comp_date)

'''
This is for Complaint Dashboard Export
SafeFood -> Complaints -> Complaints Dashboard
'''
# comp_dash = pd.read_excel('ComplaintsDashboard 2020-03-09.xlsx',header=1, sheet_name='ComplaintsExport')
# comp_dash['Conducted Date'] = pd.to_datetime(comp_dash['Conducted Date'])


cols_to_skip = ['Criteria','Risk Value (R)','Uncertainty (U)','Total R+(Max(R)xU)','Report']
cols_to_use = ['No.', 'Date', 'Name', 'Nonconformance', 'Source', 'Status', 'Unnamed: 6', 'Responsible (Investigation)', 'Responsible (Review)', 'Due Date', 'Report', 'Unnamed: 15', 'Details', 'Root Cause', 'Date.1', 'Report.1', 'Action Required', 'Type', 'Responsible', 'Deadline', 'Action Taken', 'Completed By', 'Unnamed: 26',
       'Completed', 'Date.2', 'Report.2', 'Report.3', 'Completed.1']

ca = pd.read_excel('CorrectiveActionExport2020-03-09.xlsx', usecols=cols_to_use)
#used this once to get list
# col_to_use = [y for y in ca.columns if y not in cols_to_skip]

col_ff = ['No.','Date','Name','Nonconformance','Source']

ffill(ca, col_ff)

ca = ca.dropna(how='all',axis=1)


print('ehl')
