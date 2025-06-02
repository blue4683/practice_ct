import sys
input = sys.stdin.readline
INF = 10 ** 9


def floyd(arr):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    return arr


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

edges = [(graph[i][j], i, j) for i in range(n) for j in range(n) if i != j]
edges.sort(reverse=True)
result = 0

arr = [[INF] * n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0

while graph != arr:
    if not edges:
        result = -1
        break

    cost, i, j = edges.pop()
    if arr[i][j] > cost:
        result += cost
        arr[i][j], arr[j][i] = cost, cost
        arr = floyd(arr)

print(result)
