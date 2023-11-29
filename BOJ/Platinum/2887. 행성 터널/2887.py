import sys

input = sys.stdin.readline


class P:
    def __init__(self, n, z, y, x):
        self.n = n
        self.z = z
        self.y = y
        self.x = x


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
planets = [P(i, *map(int, input().split())) for i in range(n)]
graph = [i for i in range(n + 1)]
result = 0
edges = []

planets.sort(key=lambda x: x.x)
for i in range(n - 1):
    edges.append([planets[i].n, planets[i + 1].n, abs(planets[i].x - planets[i + 1].x)])

planets.sort(key=lambda x: x.y)
for i in range(n - 1):
    edges.append([planets[i].n, planets[i + 1].n, abs(planets[i].y - planets[i + 1].y)])

planets.sort(key=lambda x: x.z)
for i in range(n - 1):
    edges.append([planets[i].n, planets[i + 1].n, abs(planets[i].z - planets[i + 1].z)])

edges.sort(key=lambda x: x[-1])


for now, next, cost in edges:
    if find(now) != find(next):
        union(now, next)
        result += cost

print(result)
