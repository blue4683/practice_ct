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


n = int(input())
graph = [i for i in range(n + 1)]
for _ in range(n - 2):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

parents = set()
for i in range(1, n + 1):
    parents.add(find(i))

print(*parents)
