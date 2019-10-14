# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 求最大公约数

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor


with ThreadPoolExecutor(max_workers=1) as executor:
    start = time.time()
    future = executor.submit(pow, 323, 1235)
    end = time.time()
    print(future.result())
    print('Took %.3f seconds.' % (end - start))
