import sys
input = sys.stdin.readline


def multiply(a, b):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            value = 0
            for k in range(n):
                value += a[i][k] * b[k][j]

            matrix[i][j] = value % 1000

    return matrix


def square(matrix, b):
    if b == 1:
        return matrix

    elif b == 2:
        return multiply(matrix, matrix)

    else:
        new_matrix = square(matrix, b // 2)
        new_matrix = multiply(new_matrix, new_matrix)
        if b % 2:
            return multiply(new_matrix, matrix)

        else:
            return new_matrix


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix = [list(map(lambda x: x % 1000, mat)) for mat in square(matrix, b)]
for mat in matrix:
    print(*mat)
