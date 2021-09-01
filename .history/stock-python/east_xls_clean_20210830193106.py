import os
import pandas as pd
"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""

f1 = 'stock_hs_0830.xls'

orig_dir = r'C:\Users\hxm\Downloads\eastmoney_xls'
orig_file = os.path.join(orig_dir, f1)
sav_dir = r'C:\Users\hxm\Downloads\eastmoney_xls\cleaned'
savename = f1[:-4] + '_clearn.xls'
print(savename)

print(orig_file)
# sav_filename
# pd.read_csv(r'')