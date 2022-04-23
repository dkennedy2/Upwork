# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:36:04 2022

@author: cc-ch
"""

import pandas as pd
df = pd.read_csv(r'C:\Users\cc-ch\Desktop\Upwork\Windfarms\data.csv')

# convert strings to datetime
df['end_date'] = pd.to_datetime(df['end_date'])
df['start_date'] = pd.to_datetime(df['start_date'])


df['installation_time'] = df['end_date']  - df['start_date']
for index, row in df['installation_time']
    df['days'] = df['installation_time'].days
    df['hours'] = df['installation_time'].hours
