import sys
input = sys.stdin.readline


def dfs(day, weight, visited):
    global result
    if weight < 500:
        return

    if day == n:
        result += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(day + 1, weight + weights[i] - k, visited)
        visited[i] = 0


n, k = map(int, input().split())
weights = list(map(int, input().split()))

result = 0
dfs(0, 500, [0] * n)
print(result)
