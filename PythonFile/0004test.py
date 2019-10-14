import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


# def main():
#     for number in PRIMES:
#         if is_prime(number):
#             print('%d is prime' % (number))
#         else:
#             print('%d is not prime' % (number))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('Took %.3f seconds.' % (end - start))
