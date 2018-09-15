# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:24:32 2018

@author: disiz
"""
#1) How-to-count-distance-to-the-previous-zero
import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
b_temp=[]
z_pos = -1
for i, n in enumerate(df.X):
    if n == 0:
        z_pos = i
    b_temp.append(i - z_pos)
df['Y']=b_temp
print(df)
print("-"*80)
#2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a
#Series of random numbers.
import pandas as pd
from numpy.random import randn
s= pd.Series(randn(len(pd.bdate_range('2015-01-01', '2015-12-31'))), index=pd.bdate_range('2015-01-01', '2015-12-31'))
print("pandas series\n",s)
print("-"*80)
#3) Find the sum of the values in s for every Wednesday
s_weekdays = s.groupby([lambda x: x.weekday]).sum()
print("sum of values for weekdays\n",s_weekdays) 
s_wednesday=s_weekdays[2] #0-Mon,1-Tue,2-Wed,3-Thu,4-Fri,5-Sat,6-Sun
print("sum of values for day-wednesday",s_wednesday) 
print("-"*80)
#4) Average For each calendar month
s_months = s.groupby([lambda x: x.month]).mean()
print("average of values for months\n",s_months)
print("-"*80)
#5) For each group of four consecutive calendar months in s, find the date on which the
#highest value occurred.
s_max = s.groupby([lambda x: x.month]).max()
print("maximum of values for months\n",s_max)
print("-"*80)
print("\nEnd of assignemnt")