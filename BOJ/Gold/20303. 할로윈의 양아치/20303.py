import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
graph = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

candies = []
visited = [0] * (n + 1)
for i in range(1, n + 1):
    if visited[i]:
        continue

    visited[i] = 1
    cnt, candy = 1, arr[i]
    for j in range(i + 1, n + 1):
        if find(i) == find(j):
            visited[j] = 1
            cnt += 1
            candy += arr[j]

    candies.append((cnt, candy))

dp = [0] * (k)
for cnt, candy in candies:
    for j in range(k - 1, -1, -1):
        if not j and cnt < k:
            dp[cnt] = max(dp[cnt], candy)

        elif j and dp[j]:
            if j + cnt < k:
                dp[j + cnt] = max(dp[j + cnt], dp[j] + candy)

print(max(dp))
