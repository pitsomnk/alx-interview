#!/usr/bin/python3
"""Module to rotate a 2D matrix 90 degrees clockwise."""

def rotate_2d_matrix(matrix):
    """Rotate the given n x n 2D matrix 90 degrees clockwise."""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

