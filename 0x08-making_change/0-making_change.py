#!/usr/bin/python3
"""Module that returns least amount of coins
to fill the pile"""


def makeChange(coins, total):
    """function that returns least number of coins
    needed to fill the pile"""
    coins = sorted(coins, reverse=True)
    index = 0
    count = 0
    while total > 0:
        if index >= len(coins):
            return -1
        if total - coins[index] >= 0:
            total -= coins[index]
            count += 1
        else:
            index += 1
    return count
