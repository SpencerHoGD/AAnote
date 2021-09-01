import psycopg2
import pandas as pd
import tushare as ts
import datetime

"""download daily stock data from tushare, insert into progresql database, and check sum(amount)"""


def insertOperate(today):
    start_date = '{} 00:00:00'.format(today)
    end_date = '{} 23:59:59'.format(today)
    print(start_date, end_date)

    conn = psycopg2.connect(database='postgres', user='postgres',password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')

    db1 = 'daily'
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    date_ts = str(today).replace('-', '')
    df = pro.daily(date_ts)
    print(df.shape())





if __name__ == "__main__":
    today = datetime.date.today()
    insertOperate(today)