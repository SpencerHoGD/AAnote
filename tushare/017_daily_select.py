import psycopg2 
import pandas as pd 
import tushare as ts 
# from sqlalchemy import create_engine 



def selectOperate():
    db2 = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    # cursor.execute("select * from {}".format(db2))
    cursor.execute("select * from {} where trade_date between \
        '2017-12-27 00:00:00' and '2017-12-28 23:59:59' ".format(db2))
    rows = cursor.fetchall()
    print(len(rows))
    # for row in rows[-10:]:
    # for row in rows[:10]:
    #     print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], \
    #           row[7], row[8], row[9], row[10])
    conn.close()


if __name__ == "__main__":
    # selectOperate()
