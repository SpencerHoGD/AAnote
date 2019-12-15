import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
# import psycopg2
# import matplotlib.pyplot as plt


def connectPostgreSQL():
    db1 = 'new_share'
    ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
    pro = ts.pro_api()

    year1 = 2000
    year2 = 2009
    start_date = '{}0101'.format(year1)
    end_date = '{}1231'.format(year2)
    df = pro.new_share(start_date=start_date, end_date=end_date)

    engine = create_engine(
        'postgresql://postgres:394460@localhost:5432/postgres')
    print('connect successfully')
    df.to_sql(name=db1, con=engine, index=False, if_exists='append')


if __name__ == "__main__":
    connectPostgreSQL()
