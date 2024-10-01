#!/usr/bin/pyhon3

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1 for _ in range(i+1)] for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle


