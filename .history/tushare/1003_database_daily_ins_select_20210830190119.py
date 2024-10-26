import psycopg2
import pandas as pd
import tushare as ts
import datetime

"""download daily stock data from tushare, insert into progresql database, and check sum(amount)"""


def insertOperate(today):
    # start_date = '{} 00:00:00'.format(today)
    # end_date = '{} 23:59:59'.format(today)
    # print(start_date, end_date)

    conn = psycopg2.connect(database='postgres', user='postgres',password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    # print('connect successful!')

    db1 = 'daily'
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()
    date_ts = str(today).replace('-', '')
    df = pro.daily(trade_date=date_ts)
    # df.to_csv(r'C:\Users\hxm\Downloads\eastmoney_xls\ts_daily_20210830.csv')

    ts_code = df['ts_code'].tolist()
    trade_date = df['trade_date'].tolist()
    open_p = df['open'].tolist()
    high_p = df['high'].tolist()
    low_p = df['low'].tolist()
    close_p = df['close'].tolist()
    pre_close = df['pre_close'].tolist()
    change = df['change'].tolist()
    pct_chg = df['pct_chg'].tolist()
    vol = df['vol'].tolist()
    amount = df['amount'].tolist()

    count = 0
    for i in range(len(ts_code)):
        cursor.execute("""INSERT INTO daily
        (ts_code, trade_date, open_p, high_p, low_p, close_p,
        pre_close, change, pct_chg, vol, amount)
        VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                        (ts_code[i],
                        trade_date[i],
                        open_p[i],
                        high_p[i],
                        low_p[i],
                        close_p[i],
                        pre_close[i],
                        change[i],
                        pct_chg[i],
                        vol[i],
                        amount[i]))
        conn.commit()
        count += 1

    conn.close()
    print('insert {}th of {} records at {} into table "{}" successfully'\
        .format(count, len(ts_code), trade_date[0], db1))


def selectOperate(today):
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port='5432')
    db_read = 'daily'
    QL8 = "select SUM(amount) from {} where trade_date = {};".format(db_read, today)
    df = pd.read_sql(QL8, con=conn)
    conn.close()

    print(df.head())
    print(df.tail())



if __name__ == "__main__":
    today = datetime.date.today()
    insertOperate(today)