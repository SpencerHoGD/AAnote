import os
from numpy import NaN, float64, int64
import pandas as pd

"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""


def str2value(valueStr):
    valueStr = str(valueStr)
    idxOfYi = valueStr.find('亿')
    idxOfWan = valueStr.find('万')
    bar = valueStr.find(' —')
    if idxOfYi != -1 and idxOfWan != -1:
        return float(float(valueStr[:idxOfYi])*1e8 + float(valueStr[idxOfYi+1:idxOfWan])*1e4)
    elif idxOfYi != -1 and idxOfWan == -1:
        return float(float(valueStr[:idxOfYi])*1e8)
    elif idxOfYi == -1 and idxOfWan != -1:
        return float(float(valueStr[:idxOfWan])*1e4)
    elif idxOfYi == -1 and idxOfWan == -1:
        return float(valueStr)
    elif bar != -1:
        return None


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

collist = [x for x in dn.columns]
cols2 = [5, 6, 11, 21, 23, 24, 26, 27, 29, 30, 31, 32]
cols3 = []
for cl in cols2:
    cols3.append(collist[cl])
    for cl1 in cols3:
        dn[cl1] = dn[cl1].str.strip()
    
# dn.现量 = dn.现量.apply(str2value)
new_col = []
for xl in dn.金额:
    if xl == '—':
        xl = 0
    elif str(xl).find('亿') != -1:
        xl = int64(float(str(xl).strip('亿'))*1e8)
    elif str(xl).find('万') != -1:
        xl = int64(float(str(xl).strip('万'))*1e4)
    else:
        xl = int(xl)
    new_col.append(xl)

print(new_col)


# print(dn.现量)

# print(dn)
# dn.iloc[:, [5]] = dn.iloc[:, [5]].apply(str2value)




# dn.to_csv(p2)

res = dn
# res = dn.iloc[:6, [-1]]
# print(res)
# print(res.columns)
# print(res.describe)
# print(res.info())
# print(res.dtypes)
# print(res.head())
# print(res.tail())
# print(res.shape)
