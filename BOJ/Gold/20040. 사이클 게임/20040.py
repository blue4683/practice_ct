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


n, m = map(int, input().split())
graph = [i for i in range(n)]
result = 0
for t in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        result = t + 1
        break

    union(a, b)

print(result)
