from collections import deque
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


n = int(input())
weight = [[0] + [int(input()) for _ in range(n)]]
for i in range(1, n + 1):
    weight.append([weight[0][i]] + list(map(int, input().split())))

graph = [i for i in range(n + 1)]
edges = [(y, x, weight[y][x]) for y in range(n + 1)
         for x in range(n + 1) if y != x]
edges.sort(key=lambda x: x[-1])

result = 0
for y, x, cost in edges:
    if find(y) == find(x):
        continue

    union(y, x)
    result += cost

print(result)
