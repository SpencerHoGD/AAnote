
import os
d1 = r'C:\Users\hxm\Downloads\eastmoney_xls'
f4 = 'delete_symbol.xls'
p4 = os.path.join(d1, f4)
print(p4)

df = pd.read_csv(p4)