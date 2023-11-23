import sys

input = sys.stdin.readline

MOD = 1000000007


def matrix_multiply(A, B):
    matrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] = (matrix[i][j] + A[i][k] * B[k][j]) % MOD

    return matrix


n = int(input())

result = [[1, 0], [0, 1]]
matrix = [[1, 1], [1, 0]]

while n:
    if n & 1:
        result = matrix_multiply(result, matrix)
    matrix = matrix_multiply(matrix, matrix)
    n //= 2

print(result[0][1])
