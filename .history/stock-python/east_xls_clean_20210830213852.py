import os
import pandas as pd
import openpyxl

"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""

d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
f1 = 'stock_hs_0830.xls'
p1 = os.path.join(d1, f1)

d2 = d1 + r'\clearned'
f2 = f1[:-4] + '_clearn.scv'
p2 = os.path.join(d2, f2)
# print(p1, d2, f2, p2, sep='\n')
print(p1)

# with open(p1,'r') as f:
    # df = pd.read_excel(f)
#     # df = pd.read_excel(p1, engine='unicode_escape' )
    # print(df.info())

# df = pd.read_excel(r"C:\Users\hxm\Downloads\eastmoney_xls\stock_hs_0830.xls", encoding='unicode_escape' )
df = pd.read_excel(r'C:\Users\hxm\Downloads\eastmoney_xls\stock_hs_0830.xls', engine='xlrd')
# print(df.info())