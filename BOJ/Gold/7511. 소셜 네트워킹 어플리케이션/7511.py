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


for t in range(int(input())):
    n, k = int(input()), int(input())
    graph = [i for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)

    print(f'Scenario {t + 1}:')
    for _ in range(int(input())):
        u, v = map(int, input().split())
        print(int(find(u) == find(v)))

    print()
