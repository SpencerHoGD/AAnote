import psycopg2 
import pandas as pd 
import tushare as ts 
# from sqlalchemy import create_engine 


def connectPostgreSQL():
    db = 'trade_cal'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    print('connect successful!')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE {}
                                      (exchange 	 VARCHAR(10),
                                       cal_date          date, 
                                       is_open            smallint, 
                                       PRIMARY KEY (cal_date)
                                        );""".format(db))
    conn.commit()
    conn.close()
    print('table {} is created!'.format(db))


def insertOperate():
    db = 'trade_cal'
    ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
    pro = ts.pro_api()

    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')

    df = pro.query('trade_cal', start_date='19900101', end_date='20191231')

    exchange = df['exchange'].tolist()
    cal_date = df['cal_date'].tolist()
    is_open = df['is_open'].tolist()
    count = 0
    for i in range(len(exchange)):
        # cursor.execute("""INSERT INTO trade_cal
        cursor.execute("""INSERT INTO trade_cal
        (exchange, cal_date, is_open)
        VALUES(%s, %s, %s);""",
                     (exchange[i],
                      cal_date[i],
                      is_open[i]))
        conn.commit()
        print("已插入第{0}行，共有{1}行".format(count, len(exchange)))
        count += 1 

    conn.close()
    print('insert records into {db} successfully')


def selectOperate():
    db = 'trade_cal'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {}".format(db))
    rows = cursor.fetchall()
    for row in rows[:10]:
        print(row)
    conn.close()


def select_trade_date():
    db = 'trade_cal'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    cursor.execute("select cal_date from {} where is_open = 1".format(db))
    rows = cursor.fetchall()
    for row in rows[:10]:
        print(row)
    conn.close()



if __name__ == "__main__":
    # connectPostgreSQL()
    # insertOperate()
    # selectOperate()
    select_trade_date()
