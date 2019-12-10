import psycopg2


con = psycopg2.connect(database="postgres", user="postgres", password="394460", host="127.0.0.1", port="5432")  
print("Database opened successfully")
cur = con.cursor()  

# cur.execute("""CREATE TABLE 沪深300指数日线行情
#                                   (ts_code          VARCHAR(10)      NOT NULL,
#                                    trade_date       DATE             NOT NULL,
#                                    open_p           NUMERIC          DEFAULT 0,
#                                    high_p           NUMERIC          DEFAULT 0,
#                                    low_p            NUMERIC          DEFAULT 0,
#                                    close_p          NUMERIC          DEFAULT 0,
#                                    pre_close        NUMERIC          DEFAULT 0,
#                                    pct_chg          NUMERIC          DEFAULT 0,
#                                    PRIMARY KEY (ts_code, trade_date)
#                                     );""")
cur.execute("""CREATE TABLE 沪深股票qfq日线行情
                                  (ts_code          VARCHAR(10)      NOT NULL,
                                   trade_date       DATE             NOT NULL,
                                   open_p           NUMERIC          DEFAULT 0,
                                   high_p           NUMERIC          DEFAULT 0,
                                   low_p            NUMERIC          DEFAULT 0,
                                   close_p          NUMERIC          DEFAULT 0,
                                   pre_close        NUMERIC          DEFAULT 0,
                                   pct_chg          NUMERIC          DEFAULT 0,
                                   PRIMARY KEY (ts_code, trade_date)
                                    );""")
print("Table created successfully")
con.commit()
con.close()