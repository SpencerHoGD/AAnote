import os
import pandas as pd


d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
# f4 = 'delete_symbol.xlsx'
f4 = 'delete_symbol.csv'
p4 = os.path.join(d1, f4)
print(p4)

# sdsym = pd.read_csv(p4, encoding='ANSI')
sdsym = pd.read_csv(p4)
# print(sdsym.head())
print(sdsym.info())