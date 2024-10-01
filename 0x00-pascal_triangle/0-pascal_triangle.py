#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows using both for and while loops.
    
    Args:
        n (int): The number of rows to generate.
    
    Returns:
        list of lists: Pascal's triangle represented as a list of lists of integers.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    row_index = 1
    
    while row_index < n:
        previous_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, row_index):
            new_row.append(previous_row[j-1] + previous_row[j])
        
        new_row.append(1)
        triangle.append(new_row)
        row_index += 1
    
    return triangle
