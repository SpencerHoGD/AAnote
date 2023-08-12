# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 求最大公约数

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor

# 最大公约数


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [
    (19633090, 22659730), (18796750, 24936700), (20306770, 38141720),
    (15516450, 22296200), (19889120, 47366700), (21989640, 78762930)
]

# 不使用多线程/多进程
def not_any():
    start = time.time()
    results = list(map(gcd, numbers))
    end = time.time()
    print('Took %.3f seconds.' % (end - start))


# 多线程ThreadPoolExecutor
def mulThread():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers))
    end = time.time()
    print('Took %.3f seconds.' % (end - start))


# 多进程ProcessPoolExecutor
def mulProcess():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=6)
    results = list(pool.map(gcd, numbers))
    end = time.time()
    print('Took %.3f seconds.' % (end - start))


if __name__ == '__main__':
    # not_any()
    # mulThread()
    mulProcess()