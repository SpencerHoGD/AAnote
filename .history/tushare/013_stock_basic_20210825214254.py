import psycopg2
import pandas as pd
import tushare as ts
# from sqlalchemy import create_engine


def connectPostgreSQL():
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    print('connect successful!')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE stock_basic
                                      (ts_code 	 VARCHAR(10)    NOT NULL,
                                       ts_symbol          TEXT     , 
                                       ts_name            TEXT     , 
                                       ts_area            TEXT     , 
                                       ts_industry        TEXT     , 
                                       ts_market          TEXT     , 
                                       ts_list_date       DATE     , 
                                       PRIMARY KEY (ts_code)
                                        );""")
    conn.commit()
    conn.close()
    print('table stock_basic is created!')


def insertOperate():
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')

    df = pro.stock_basic(exchange='', list_status='L')

    ts_code = df['ts_code'].tolist()
    ts_symbol = df['symbol'].tolist()
    ts_name = df['name'].tolist()
    ts_area = df['area'].tolist()
    ts_industry = df['industry'].tolist()
    ts_market = df['market'].tolist()
    ts_list_date = df['list_date'].tolist()
    count = 0
    for i in range(len(ts_code)):
        cursor.execute("""INSERT INTO stock_basic
        (ts_code, ts_symbol, ts_name, ts_area, ts_industry, ts_market, ts_list_date)
        VALUES( %s, %s, %s, %s, %s, %s, %s);""",
                       (ts_code[i],
                        ts_symbol[i],
                        ts_name[i],
                        ts_area[i],
                        ts_industry[i],
                        ts_market[i],
                        ts_list_date[i]))
        conn.commit()
        count += 1

    conn.close()
    print("已插入第{0}行，共有{1}行".format(count, len(ts_code)))
    print('insert records into stock_basic successfully')


def selectOperate():
    db1 = 'stock_basic'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {}".format(db1))
    rows = cursor.fetchall()
    for row in rows[-10:]:
        print(row)
    conn.close()


def updateOperate():
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    cursor.execute("update public.member set name='update ...' where id=2")
    conn.commit()
    print("Total number of rows updated :", cursor.rowcount)

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    conn.close()


def deleteOperate():
    db1 = 'stock_basic'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()


    print('begin delete')
    cursor.execute("delete * from {}".format(db1))
    # cursor.execute("delete from public.member where id=4")
    conn.commit()   
    print('end delete')
    print("Total number of rows deleted :", cursor.rowcount)
    
    conn.close()


if __name__ == "__main__":
    # connectPostgreSQL()
    # insertOperate()
    # selectOperate()
    # updateOperatje()
    deleteOperate()
