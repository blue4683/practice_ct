import sys
input = sys.stdin.readline


def check(arr):
    wormhole = [0] * n
    for i in range(0, n, 2):
        a, b = arr[i:i + 2]
        wormhole[a] = b
        wormhole[b] = a

    for start in range(n):
        visited = [0] * n
        q = [start]
        while q:
            now = q.pop()
            teleported = wormhole[now]
            if visited[teleported]:
                return 1

            visited[teleported] = 1
            moved = graph[teleported]
            if moved == -1:
                continue

            q.append(moved)

    return 0


def dfs(arr, visited):
    global result
    if len(arr) == n:
        if check(arr):
            result += 1

        return

    u = -1
    for i in range(n):
        if not visited[i]:
            u = i
            break

    visited[u] = 1
    arr.append(u)

    for v in range(u + 1, n):
        if visited[v]:
            continue

        arr.append(v)
        visited[v] = 1
        dfs(arr, visited)
        arr.pop()
        visited[v] = 0

    arr.pop()
    visited[u] = 0


n = int(input())
wormholes = [tuple(map(int, input().split())) for _ in range(n)]
wormholes.sort()

graph = [-1] * n
for i in range(n):
    x1, y1 = wormholes[i]
    for j in range(i + 1, n):
        x2, y2 = wormholes[j]
        if y1 == y2 and x1 < x2:
            graph[i] = j
            break

result = 0
dfs([], [0] * n)
print(result)
