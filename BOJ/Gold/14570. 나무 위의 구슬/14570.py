import sys
input = sys.stdin.readline


n = int(input())
graph = [[-1, -1] for _ in range(n + 1)]
for i in range(1, n + 1):
    u, v = map(int, input().split())
    graph[i][0] = u
    graph[i][1] = v

k = int(input())
cur = 1
while 1:
    if graph[cur] == [-1, -1]:
        break

    elif graph[cur][0] == -1:
        cur = graph[cur][1]

    elif graph[cur][1] == -1:
        cur = graph[cur][0]

    else:
        if k % 2:
            cur = graph[cur][0]
            k = (k + 1) // 2

        else:
            cur = graph[cur][1]
            k //= 2

print(cur)
