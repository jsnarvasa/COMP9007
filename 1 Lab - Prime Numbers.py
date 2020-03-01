"""
Given n number, return if it is prime or not
"""
import random
import math

def is_prime(n=random.randint(2,1000000)):
    if n == 1:
        return False

    for num in range(2,n):
        if n % num == 0:
            return False
    return True


def is_prime_sqrt(n=random.randint(2,1000000)):
    if n == 1:
        return False

    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0:
            return False
    return True


def is_prime_sqrtv2(n=random.randint(2,1000000)):
    if n == 1:
        return False

    n_sqrt = math.floor(math.sqrt(n))
    for num in range(2, n_sqrt):
        if n % num == 0:
            return False
    return True


def is_prime_sqrt_odd(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return False

    for num in range(3, math.floor(math.sqrt(n))):
        if n % num == 0:
            return False
    return True


import time
max_num = 10000

start = time.time()
for n in range(1, max_num):
    is_prime(n)
end = time.time()
print(f"Time taken for 2 to n: {end - start}")

start = time.time()
for n in range(1, max_num):
    is_prime_sqrt(n)
end = time.time()
print(f"Time taken for 2 to sqrt(n): {end - start}")

start = time.time()
for n in range(1, max_num):
    is_prime_sqrtv2(n)
end = time.time()
print(f"Time taken for 2 to sqrt(n) v2: {end - start}")

start = time.time()
for n in range(1, max_num):
    is_prime_sqrt_odd(n)
end = time.time()
print(f"Time taken for 2 to sqrt(n) odd: {end - start}")