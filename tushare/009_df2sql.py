from sqlalchemy import create_engine
import pandas as pd
import tushare as ts


ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
pro = ts.pro_api()
engine = create_engine('postgresql://postgres:394460@localhost:5432/postgres')
print('Database opened successfully')
code_list = ['000001.SZ', '000002.SZ']
for i in code_list:
    print(i)
    df = ts.pro_bar(ts_code=i, adj='qfq', start_date='20190501', end_date='20190531')
    df.to_sql(name='沪深股票qfq日线行情', con=engine, index=False, if_exists='append')


# df_index = pd.read_sql("SELECT ts_code, trade_date, close_p FROM 沪深300指数日线行情;", con=engine)
df_index = pd.read_sql("SELECT * FROM 沪深股票qfq日线行情;", con=engine)
print(df_index)
# print(df_index.head())