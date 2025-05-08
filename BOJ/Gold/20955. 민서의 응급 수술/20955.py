import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = map(find, [x, y])
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

result = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(u) != find(v):
        union(u, v)

    else:
        result += 1

for x in range(1, n + 1):
    find(x)

result += len(set(graph)) - 2
print(result)
