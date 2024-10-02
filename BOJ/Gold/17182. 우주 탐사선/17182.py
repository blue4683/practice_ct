import sys
input = sys.stdin.readline
INF = 10 ** 9


def dfs(now, cost, visited):
    global result
    if cost >= result:
        return

    if visited == (1 << n) - 1:
        result = min(result, cost)
        return

    for next_planet in range(n):
        if visited & (1 << next_planet):
            continue

        dfs(next_planet, cost + planets[now]
            [next_planet], visited | (1 << next_planet))


n, k = map(int, input().split())
planets = [list(map(int, input().split())) for _ in range(n)]

for mid in range(n):
    for start in range(n):
        for end in range(n):
            planets[start][end] = min(
                planets[start][end], planets[start][mid] + planets[mid][end])

result = INF
dfs(k, 0, 1 << k)
print(result)
