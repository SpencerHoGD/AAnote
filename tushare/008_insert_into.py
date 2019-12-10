import psycopg2
import pandas as pd
import tushare as ts


con = psycopg2.connect(database="postgres", user="postgres", password="394460", host="127.0.0.1", port="5432")
print("Database opened successfully")
cur = con.cursor()


ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
pro = ts.pro_api()
# 单位：涨跌幅（%）, 成交量（手）、成交额（千元）
df = pro.index_daily(ts_code='399300.SZ', start_date='20150501', end_date='20191231')
ts_code = df['ts_code'].tolist()
trade_date = df['trade_date'].tolist()
open_p = df['open'].tolist()
high_p = df['high'].tolist()
low_p = df['low'].tolist()
close_p = df['close'].tolist()
pre_close = df['pre_close'].tolist()
pct_chg = df['pct_chg'].tolist()
count = 0
for i in range(len(ts_code)):
    cur.execute("""INSERT INTO 沪深300指数日线行情 
    (ts_code, trade_date, open_p, high_p, low_p, close_p, pre_close, pct_chg)
    VALUES( %s, %s, %s, %s, %s, %s, %s, %s);""",
                 (ts_code[i],
                  trade_date[i],
                  open_p[i],
                  high_p[i],
                  low_p[i],
                  close_p[i],
                  pre_close[i],
                  pct_chg[i]))
    con.commit()
    print("已插入第{0}行，共有{1}行".format(count, len(ts_code)))
    count += 1 