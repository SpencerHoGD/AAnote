#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-04
hexiaoming
'''
import numpy as np
import pandas as pd
import string
import os
from os import path
import urllib

d = path.dirname(__file__)
index_num = 52
half_num = index_num // 2
col_num = list(string.ascii_uppercase)[:half_num]
r = '\n Hello world! \n'

dates = pd.date_range('20191001', periods=index_num, freq='H')
df = pd.DataFrame(np.random.randn(index_num, half_num),
                  index=dates, columns=col_num)

r = df

#r = df.sort_values(by='B')
#r = df.sort_index(axis=1, ascending=False)
#r = df[0:3]
#r = df.T
#r = df.describe()
#r = df.to_numpy()
#r = df.head()
#r = df.tail()

#r = df.loc[dates[0]]
#r = df.loc[:, ['A', 'B']]
#r = df.loc['20191004':'20191007', ['A', 'B']]
#r = df.loc[dates[0], 'A']
#r = df.at[dates[0], 'A']
#r = df.iloc[3:5, 0:2]
#r = df.iloc[3:5, :]
#r = df.iloc[[1, 2, 4], [0, 2]]
#r = df[df.A > 0]
#r = df[df > 0]
#r.to_csv(path.join(d, 'pandas_dataframe_csv.csv'))
#r.to_excel(path.join(d, 'pandas_dataframe_excel.xls'))
# print(r)
