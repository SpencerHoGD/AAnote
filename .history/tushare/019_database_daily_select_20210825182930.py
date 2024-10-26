import psycopg2
import pandas as pd
import tushare as ts


def selectOperate():
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port='5432')

    db1 = 'daily'

    QL1 = "select * from {};".format(db1)
    QL2 = "SELECT ts_code, trade_date, close_p FROM {};".format(db1)
    QL3 = "select * from {} where trade_date between \
           '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    QL4 = "select ts_code, trade_date, close_p from {} where trade_date between \
           '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    QL5 = "select trade_date, close_p from {} where ts_code = '{}' \
           ORDER BY trade_date ASC".format(db1, '000001.sh')
    QL6 = "select trade_date from {} ORDER BY trade_date ASC".format(db1)
    QL7 = "select ts_code, trade_date, close_p from {} where trade_date =  \
           '2021-08-25' ORDER BY ts_code ASC;".format(db1)
    QL6 = "select SUM(amount) from {} where trade_date = '2021-08-25';".format(db1)

#     df = pd.read_sql(QL1, con=conn)
    # df = pd.read_sql(QL2, con=conn)
    # df = pd.read_sql(QL3, con=conn)
    # df = pd.read_sql(QL4, con=conn)
    # df = pd.read_sql(QL5, con=conn)
    # df = pd.read_sql(QL6, con=conn)
    df = pd.read_sql(QL7, con=conn)

    print(df.tail())

    conn.close()


if __name__ == "__main__":
    selectOperate()
