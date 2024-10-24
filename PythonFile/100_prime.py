import math
import time

"""
7.7 seconds
2.272 sec lian-arch
"""


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


start = time.time()

# for num in range(2, 200):
#     if is_prime(num):
#         print(num, end=' ')

for num in range(2, 2000000):
    if is_prime(num):
        pass

end = time.time()
print('Took %.3f seconds.' % (end - start))
