import psycopg2
import pandas as pd
import tushare as ts
# from sqlalchemy import create_engine


def select_trade_date():
    # start_date = '2018-01-01'
    # end_date = '2018-06-30'
    start_date = '2018-07-01'
    end_date = '2018-12-31'

    db1 = 'trade_cal'
    trade_date = []

    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {} where cal_date between \
                   '{} 00:00:00' and '{} 23:59:59' and is_open = 1"
                   .format(db1, start_date, end_date))
    rows = cursor.fetchall()
    # for row in rows[:10]:
    for row in rows:
        date = str(row[1]).replace('-', '')
        trade_date.append(date)
    conn.close()
    print(trade_date.__len__())


def insertOperate():
    # 已存2013-2019年
    year = 2014
    start_date = '{}-01-01'.format(year)
    end_date = '{}-06-30'.format(year)
    # start_date = '{}-07-01'.format(year)
    # end_date   = '{}-12-31'.format(year)
    # start_date = '2019-07-01'
    # end_date   = '2019-11-30'

    db1 = 'trade_cal'
    trade_date = []

    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {} where cal_date between \
                   '{} 00:00:00' and '{} 23:59:59' and is_open = 1"
                   .format(db1, start_date, end_date))
    rows = cursor.fetchall()
    for row in rows:
        date = str(row[1]).replace('-', '')
        trade_date.append(date)

    db2 = 'daily'
    ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
    pro = ts.pro_api()

    for date1 in trade_date:
        df = pro.daily(trade_date=date1)
        # df = pro.daily(trade_date = '20191129')

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
    print('insert records into table successfully')
    # print('insert {}th of {} records at {} into table "{}" successfully'\
    #     .format(count, len(ts_code), trade_date[0], db2))


def selectOperate():
    year = 2013
    db2 = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {}".format(db2))
    # cursor.execute("select * from {} where trade_date between \
    #     '{}-12-27 00:00:00' and '{}-12-28 23:59:59' ".format(db2, year, year))
    # cursor.execute("select * from {} where trade_date between \
    #     '{}-06-21 00:00:00' and '{}-06-30 23:59:59' ".format(db2, year, year))
    rows = cursor.fetchall()
    print(len(rows))
    # for row in rows[-10:]:
    # for row in rows[:10]:
    #     print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], \
    #           row[7], row[8], row[9], row[10])
    conn.close()


if __name__ == "__main__":
    # select_trade_date()
    # insertOperate()
    selectOperate()
