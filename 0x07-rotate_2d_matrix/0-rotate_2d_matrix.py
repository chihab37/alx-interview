#!/usr/bin/python3
"""
2D matrix rotation module.
This module provides a function to rotate an n x n 2D matrix by 90 degrees clockwise in place.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): The n x n matrix to rotate.
        
    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    rotate_2d_matrix(matrix)
    
    print("\nRotated Matrix:")
    for row in matrix:
        print(row)
