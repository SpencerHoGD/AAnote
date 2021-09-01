import os, xlrd, xlwt
import pandas as pd
import openpyxl
from openpyxl import Workbook,load_workbook

"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""

d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
f1 = 'stock_hs_0830.xls'
p1 = os.path.join(d1, f1)

d2 = d1 + r'\clearned'
f2 = f1[:-4] + '_clearn.csv'
p2 = os.path.join(d2, f2)
# print(p1, d2, f2, p2, sep='\n')
# print(p1)

f3 = 'stock_hs_0830.csv'
p3 = os.path.join(d1, f3)

# with open(p1, 'r', encoding='ANSI') as f:
    # f.

df = pd.read_csv(p1, encoding='ANSI')
# print(df.columns)
new_col = df.columns.str.split('\\t').to_list()
print(new_col[1])

# s = df.iloc[:, 0]
# spls= s.str.split('\\t', expand=True)
# print(spls)

# print(df.info())
# print(df.tail())
# print(df.dtypes)
# df = pd.read_table(p3, encoding='ANSI', sep='\t', error_bad_lines=False)   # too many mistake