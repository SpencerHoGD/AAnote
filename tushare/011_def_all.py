import os 
import sys 
import psycopg2 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine 


def ts_pro_api():
    ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
    pro = ts.pro_api()
    return pro


def connectPostgreSQL():
    conn = psycopg2.connect(database='postgres', user='postgres', 
                            password='394460', host='127.0.0.1', port=5432)
    print('connect successful!')
    
    cursor=conn.cursor()
    cursor.execute('''create table public_member(
                                                 id       integer       not null   primary key,
                                                 name     varchar(32)   not null,
                                                 password varchar(32)   not null,
                                                 singal   varchar(128)
                                                 );''')
    conn.commit()
    conn.close()
    print('table public.member is created!')


def close_db_connection(conn):
    conn.commit()
    conn.close()
    

def create_one_engine():
    engine = create_engine('postgresql://postgres:394460@localhost:5432/postgres')
    print('Database opened successfully')
    

    
if __name__ == "__main__":
    # ts_pro_api()
    connectPostgreSQL()

