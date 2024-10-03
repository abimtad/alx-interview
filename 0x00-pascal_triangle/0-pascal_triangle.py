#!/usr/bin/python3
"""
 Pascal's Triangle
"""


def pascal_triangle(n):
    """A function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    response = []
    if n > 0:
    	for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                elif i > 0 and j > 0:
                    row.append(response[i - 1][j - 1] + response[i - 1][j])
            response.append(row)
    return response
