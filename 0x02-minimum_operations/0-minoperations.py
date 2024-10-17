#!/usr/bin/python3
"""A Module to calculate Minimum Operations"""


def primeFactorization(x):
    """Returns prime factorization elements of x"""
    divisor = 2
    array = list()
    while (divisor <= x):
        if x % divisor == 0:
            array.append(divisor)
            x /= divisor
        else:
            divisor += 1

    return array


def minOperations(n):
    """Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""
    minimum = 0
    factors = [y for y in primeFactorization(n)]
    occurences = {item: factors.count(item) for item in factors}
    for l, m in occurences.items():
        minimum += l * m
    return minimum
