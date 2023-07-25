import math
import time
"""
23.58 seconds
home windows 17.776 seconds
Liam-arch 7.368 seconds
"""

start = time.time()
for num in range(2, 2000000):
    is_prime = True
    for factor in range(2, int(math.floor(math.sqrt(num))) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        pass
        # print(num, end=' ')


end = time.time()
print('Took %.3f seconds.' % (end - start))
