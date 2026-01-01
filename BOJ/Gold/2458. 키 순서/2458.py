import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
arr = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1

for mid in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if arr[s][e] > arr[s][mid] + arr[mid][e]:
                arr[s][e] = arr[s][mid] + arr[mid][e]

result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF and arr[j][i] == INF:
            break

    else:
        result += 1

print(result)
