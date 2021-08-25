import math
import time
from timeit import timeit
"""
print_count = 0.69 seconds
print_count = 0.49 seconds

计算给定范围 n 内生成素数的个数
以及程序运行时间
"""


def prime_count(n):
    count = 0
    # prime = []
    # for i in range(n+1):
    #     prime.append(True)
    prime = [True] * (n+1)
    for i in range(2, int(n ** .5 + 1.5)):
        if prime[i]:
            # print(i, end=' ')
            count += 1
            j = i * i
            while j <= n:
                prime[j] = False
                j += i
    print("\n", count)


def prime_2(n):
    """
    给定 n 范围内，生成素数列表，打印列表长度（素数个数）
    """
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(2, int(n ** .5 + 1.5)):
        if not p[i]:
            continue
        for j in range(i * i, n + 1, i):
            p[j] = False
    primes = [i for i in range(n + 1) if p[i]]
    # print(primes)
    print(len(primes))


if __name__ == '__main__':
    start = time.time()
    n = 2 * 10 ** 6
    # n = 2000000
    # prime_count(n)
    prime_2(n)
    end = time.time()
    print('Took %.3f seconds.' % (end - start))
