import psycopg2
import pandas as pd
import tushare as ts
import datetime

"""download daily stock data from tushare, insert into progresql database, and check sum(amount)"""


def insertOperate(today):
  start_date = '{} 00:00:00'.format(today)
  end_date   = '{} 23:59:59'.format(today)

print(start_date, end_date)

if __name__ == "__main__":
    today = datetime.date.today()
    insertOperate(today)