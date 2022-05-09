import numpy as np


def gauss_elimination(matrix: np.array) -> np.array:
    matrix = matrix.astype('float64')
    rows, cols = matrix.shape
    if cols - 1 != rows or rows < 2:
        raise ValueError('niepoprawny rozmiar macierzy')
    for i in range(rows):
        if matrix[i, i] == 0:
            continue
        matrix[i] /= matrix[i, i]
        # for j in range(i+1, rows)
        for j in range(0, rows):
            if i != j:
                matrix[j] -= (matrix[j, i] / matrix[i, i]) * matrix[i]
    return matrix


if __name__ == '__main__':
    matrix_a = np.array([[1, 2, 3, 4], [1, 1, 9, 12], [6, 4, 12, 16]])
    print(gauss_elimination(matrix_a))
