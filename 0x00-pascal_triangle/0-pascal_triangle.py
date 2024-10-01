#!/usr/bin/python3
"""
Module that defines the pascal_triangle function
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    
    Args:
        n (int): The number of rows to generate.
    
    Returns:
        list of lists: Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for row_index in range(1, n):
        row = [1]
        for col_index in range(1, row_index):
            row.append(triangle[row_index-1][col_index-1] + triangle[row_index-1][col_index])
        row.append(1)
        triangle.append(row)
    
    return triangle
