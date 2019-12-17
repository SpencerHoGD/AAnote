from zipfile import ZipFile
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import json


filepath = r'F:\FirefoxDownloads\ExStudy.zip'
zf = ZipFile(filepath, 'r')
zf.extractall()
zf.close()

f1 = poloniex_filename = 'poloniex-trades-20190924.json'
f2 = binance_filename  = 'binance-trades-20190924.json'
f3 = coinbase_filename = 'coinbase-trades-20190924.json'
f4 = coinbene_filename = 'coinbene-trades-20190924.json'

poloniex_trades = json.loads(open(f1).read())
binance_trades  = json.loads(open(f2).read())
coinbase_trades = json.loads(open(f3).read())
coinbene_trades = json.loads(open(f4).read())

poloniex_df = pd.DataFrame({'price':[float(i['p']) for i in poloniex_trades], \
                            'size':[float(i['q']) for i in poloniex_trades], \
                            'time':[i['t'] for i in poloniex_trades]
                            })
binance_df = pd.DataFrame({'price':[float(i['p']) for i in binance_trades], \
                            'size':[float(i['q']) for i in binance_trades], \
                            'time':[i['t'] for i in binance_trades]
                            })
coinbase_df = pd.DataFrame({'price':[float(i['p']) for i in coinbase_trades], \
                            'size':[float(i['q']) for i in coinbase_trades], \
                            'time':[i['t'] for i in coinbase_trades]
                            })
coinbene_df = pd.DataFrame({'price':[float(i['p']) for i in coinbene_trades], \
                            'size':[float(i['q']) for i in coinbene_trades], \
                            'time':[i['t'] for i in coinbene_trades]
                            })

print('{} len:'.format(f1) + str(len(poloniex_trades)))
print('{} len:'.format(f2) + str(len(binance_trades)))
print('{} len:'.format(f3) + str(len(coinbase_trades)))
print('{} len:'.format(f4) + str(len(coinbene_trades)))