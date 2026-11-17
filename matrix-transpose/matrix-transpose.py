import numpy as np


def transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = []

    for j in range(cols):

        row = []
        for i in range(rows):
            row.append(A[i][j])
        result.append(row)
    
    return result

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """

    return np.array(transpose(A))