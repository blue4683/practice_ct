import sys
input = sys.stdin.readline
MOD = 10 ** 6


def multiply(a, b):
    matrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] = (matrix[i][j] + a[i][k] * b[k][j]) % MOD

    return matrix


def fibonacci(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]

    elif n == 1:
        return matrix

    else:
        new_matrix = fibonacci(matrix, n // 2)
        new_matrix = multiply(new_matrix, new_matrix)
        if n % 2:
            return multiply(new_matrix, matrix)

        else:
            return new_matrix


n = int(input())
matrix = [[1, 1], [1, 0]]
result = fibonacci(matrix, n)
print(result[0][1])
