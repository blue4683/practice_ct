import sys
input = sys.stdin.readline


def dfs(now):
    hour = 0
    next = []

    for node in graph[now]:
        next.append(dfs(node))

    next.sort(reverse=True)
    for i in range(len(next)):
        hour = max(hour, next[i] + i)

    return hour + 1


n = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    graph[arr[i]].append(i)

result = dfs(0)
print(result - 1)
