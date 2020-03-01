"""
Question: Given n number of straight cuts made on a pizza,
what's the max number of pizza slices one can produce
"""

"""
Scenario:
num_cuts, num_slices
0,1
1,2
2,4
3,7
"""

"""
The formula is therefore:
max_slices(n) = max_slices(n-1) + n
so if n == 3:
max_slices(3) = max_slices(2) + 3
max_slices(3) = max_slices(1) + 2 + 3
max_slices(3) = max_slices(0) + 1 + 2 + 3
max_slices(3) = 1 + 1 + 2 + 3 = 7

OR
Sum of first n natural number progression
max_slices(n) = [n(n+1)]/2 + 1
with formula above, can therefore prove why basecase f(0) is equal to 1


therefore:
f(12) = [12(12+1)]/2 + 1 = 79 slices for 12 cuts
"""

# Testing
import random

def max_slices_formula(n=random.randint(0,100)):
    """Given n num of straight cuts on pizza, return the max slices"""
    return n*(n-1)/2 + 1


formula_mem = {}
def max_slices_formula_memo(n=random.randint(0,100)):
    """Given n num of straight cuts on pizza, return the max slices"""
    if n in formula_mem:
        return formula_mem[n]
    return n*(n-1)/2 + 1


def max_slices_recursion(n=random.randint(0,100)):
    if n == 0:
        return 1
    return max_slices_recursion(n-1) + n


recur_mem = {}
def max_slices_recursion_memoization(n=random.randint(0,100)):
    if n in recur_mem:
        return recur_mem[n]
    else:
        if n == 0:
            val = 1
        else:
            val = max_slices_recursion_memoization(n-1) + n
        recur_mem[n] = val
        return recur_mem[n]


def dynamic_programming(n=random.randint(0,100)):
    running_total = 0
    for num in range(n+1):
        running_total += num
    return running_total


import timeit
print(f"Formula version: {timeit.timeit('max_slices_formula()', 'from __main__ import max_slices_formula')}")
print(f"Formula with memoization: {timeit.timeit('max_slices_formula_memo()', 'from __main__ import max_slices_formula_memo')}")
print(f"Recursion version: {timeit.timeit('max_slices_recursion()', 'from __main__ import max_slices_recursion')}")
print(f"Recursion with memoization: {timeit.timeit('max_slices_recursion_memoization()', 'from __main__ import max_slices_recursion_memoization')}")
print(f"Dynamic Programming: {timeit.timeit('dynamic_programming()', 'from __main__ import dynamic_programming')}")