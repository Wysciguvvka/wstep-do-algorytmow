import numpy as np


def symmetric_dist(matrix_a: np.array, matrix_b: np.array) -> int | float:
    if matrix_a.shape != matrix_b.shape:
        raise ValueError
    return np.abs(matrix_a - matrix_b).sum()


if __name__ == '__main__':
    a = np.random.randint(10, size=(5, 4))
    b = np.random.randint(10, size=(5, 4))
    print(a)
    print('---')
    print(b)
    print('---')
    print(symmetric_dist(a, b))
    print('---')
    matrix1 = np.array([[1, 1, 1], [1, 1, 1]])
    matrix2 = np.array([[1, 1, 1], [1, 1, 1]])
    print(symmetric_dist(matrix1, matrix2))
