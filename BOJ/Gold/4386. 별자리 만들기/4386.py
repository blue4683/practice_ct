import sys

input = sys.stdin.readline


class P:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def get_length(A, B):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5


def find(x):
    if x != graph[x]:
        return find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y
    else:
        graph[y] = x


n = int(input())
stars = [P(*map(float, input().split())) for _ in range(n)]
graph = [i for i in range(n + 1)]
edges = []

for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, get_length(stars[i], stars[j])])

edges.sort(key=lambda x: x[-1])

result = 0

for now, next, cost in edges:
    if find(now) != find(next):
        union(now, next)
        result += cost

print(round(result, 2))
