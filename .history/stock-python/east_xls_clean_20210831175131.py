import os
from numpy import NaN, float64, int64
import pandas as pd

"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""


d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
f1 = 'stock_hs_0830.xls'
p1 = os.path.join(d1, f1)

d2 = d1 + r'\clearned'
f2 = f1[:-4] + '_clearn.csv'
p2 = os.path.join(d2, f2)
# print(p1, d2, f2, p2, sep='\n')
# print(p2)

f3 = 'stock_hs_0830.csv'
p3 = os.path.join(d1, f3)

f4 = 'delete_symbol.csv'
p4 = os.path.join(d1, f4)

sdsym = pd.read_csv(p4)
list1 = sdsym['code'].to_list()

df = pd.read_csv(p1, encoding='ANSI')

new_col_list = df.columns.str.split('\\t').to_list()[0]

s = df.iloc[:, 0]
dfnew= s.str.split('\\t', expand=True)
dfnew.columns = new_col_list

dn = dfnew.drop(columns=[''], axis=1)
dn = dn.drop(columns=['序'], axis=1)
dn['名称'] = dn['名称'].str.strip()
dn['所属行业'] = dn['所属行业'].str.strip()
dn['代码'] = dn['代码'].str.replace('= ', '')
dn['代码'] = dn['代码'].str.replace('"', '')
dn['代码'] = dn['代码'].apply(pd.to_numeric, downcast='integer')
dn = dn[~dn['代码'].isin([i for i in list1])]
# dn['最新'] = dn['最新'].apply(pd.to_numeric, errors='coerce', downcast='float')
# dn['涨幅%'] = dn['涨幅%'].apply(pd.to_numeric, errors='coerce', downcast='float')
# dn['涨跌'] = dn['涨跌'].apply(pd.to_numeric, errors='coerce', downcast='float')
cols1 = [2, 3, 4, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 25, 28, 33, 34, 35, 36]
dn.iloc[:, [x for x in cols1]] = dn.iloc[:, [x for x in cols1]].apply(pd.to_numeric, errors='coerce', downcast='float')

def str2value(xl):    #——，亿，万，变成0或整数
    if xl == '—':
        return 0
    elif str(xl).find('亿') != -1:
        return int64(float(str(xl).strip('亿'))*1e8)
    elif str(xl).find('万') != -1:
        return int64(float(str(xl).strip('万'))*1e4)
    else:
        return int(xl)

# 处理有亿万等字眼的列，去除空格
collist = [x for x in dn.columns]
cols2 = [5, 6, 11, 21, 23, 24, 26, 27, 29, 30, 31, 32]  #有亿万字眼的列
cols3 = []
for colIndex in cols2:
    cols3.append(collist[colIndex])
    for colName in cols3:
        dn[colName] = dn[colName].str.strip()
        dn[colName] = dn[colName].apply(str2value())
    
# print(dn)
# dn.总量 = dn.总量.apply(str22value)
# print(dn.总量)

# dn.to_csv(p2)

res = dn
# res = dn.iloc[:6, [-1]]
# print(res)
# print(res.columns)
# print(res.describe)
# print(res.info())
print(res.dtypes)
print(res.head())
# print(res.tail())
# print(res.shape)
