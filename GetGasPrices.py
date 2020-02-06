'''
Created on 3 Feb 2020

@author: Margaux
'''

import pandas as pd
import urllib.request
from _datetime import timedelta

# Daily Prices CSV
# Download data from site
DayPrice_URL = 'http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls'
urllib.request.urlretrieve(DayPrice_URL, "DailyPrices.xls")

# Convert xls to csv
DayPrice_XLS = pd.read_excel('DailyPrices.xls', 'Data 1')
DayPrice_XLS.to_csv('DailyPrices.csv', index=None, header=True)

# Format data
DailyPrices_Data = pd.read_csv("DailyPrices.csv", infer_datetime_format=True)
DailyPrices_Data.columns = ['Date', 'Price (Dollars per Million Btu)']
DailyPrices_Data = DailyPrices_Data.drop([0,1], axis=0)
DailyPrices_Data['Date'] = pd.to_datetime(DailyPrices_Data['Date'])
DailyPrices_Data = DailyPrices_Data.reset_index(drop=True)

# Save to CSV
DailyPrices_Data.to_csv('Data/DailyPrices.csv')


# Monthly Prices CSV
# Download data from site
MonthPrice_URL = 'http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls'
urllib.request.urlretrieve(MonthPrice_URL, "MonthlyPrices.xls")

# Convert xls to csv
MonthPrice_XLS = pd.read_excel('MonthlyPrices.xls', 'Data 1')
MonthPrice_XLS.to_csv('MonthlyPrices.csv', index=None, header=True)

# Format Data
MonthlyPrices_Data = pd.read_csv("MonthlyPrices.csv", infer_datetime_format=True)
MonthlyPrices_Data.columns = ['Date', 'Price (Dollars per Million Btu)']
MonthlyPrices_Data = MonthlyPrices_Data.drop([0,1], axis=0)
MonthlyPrices_Data = MonthlyPrices_Data.reset_index(drop=True)
MonthlyPrices_Data['Date'] = (pd.to_datetime(MonthlyPrices_Data['Date']) + timedelta(-14))

# Save to CSV
MonthlyPrices_Data.to_csv('Data/MonthlyPrices.csv')

