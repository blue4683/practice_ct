import sys
input = sys.stdin.readline


def union(x, y):
    x, y = map(find, [x, y])
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def get_cost(edges):
    result = 0
    for x, y, cost in edges:
        if find(x) == find(y):
            continue

        union(x, y)
        result += not cost

    return result


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m + 1)]

graph = [i for i in range(n + 1)]
result1 = get_cost(sorted(edges, key=lambda x: x[-1]))

graph = [i for i in range(n + 1)]
result2 = get_cost(sorted(edges, key=lambda x: -x[-1]))

print(result1 ** 2 - result2 ** 2)
