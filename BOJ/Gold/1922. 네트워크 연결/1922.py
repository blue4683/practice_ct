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
m = int(input())
arr = [tuple(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x: x[-1])

graph = [i for i in range(n + 1)]
result = 0
for a, b, cost in arr:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)
