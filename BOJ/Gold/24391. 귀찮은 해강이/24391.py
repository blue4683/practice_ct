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
graph = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

arr = list(map(int, input().split()))
result = 0
for i in range(n - 1):
    if find(arr[i]) != find(arr[i + 1]):
        result += 1

print(result)
