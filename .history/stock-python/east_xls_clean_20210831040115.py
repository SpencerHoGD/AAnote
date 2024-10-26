import os
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

dfnew1 = dfnew.drop(columns=[''], axis=1)
dfnew1['名称'] = dfnew1['名称'].str.strip()
dfnew1['代码'] = dfnew1['代码'].str.replace('= ', '')
dfnew1['代码'] = dfnew1['代码'].str.replace('"', '')
dfnew1['代码'] = dfnew1['代码'].str
# dfnew1 = dfnew1[~dfnew1['代码'].isin([i for i in list1])]
# dfnew1.to_csv(p2)

res = dfnew1
# res = dfnew1.iloc[:6, [-1]]
print(res.head())
# print(new_col_list[38])
# print(res.columns)
# print(res.info())
# print(res.tail())
print(res.shape)

# res = dfnew1.iloc[-9:, [1, 2]]
# print(res)