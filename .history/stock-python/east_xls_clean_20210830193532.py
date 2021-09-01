import os
import pandas as pd
"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""

d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
f1 = 'stock_hs_0830.xls'

f2 = f1[:-4] + '_clearn.xls'
d2 = d1 + r'\clearned'
p1 = os.path.join(orig_dir, f1)
p2 = os.path.join(orig_dir, f1)
print(d2)
# sav_filename
# pd.read_csv(r'')