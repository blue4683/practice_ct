import sys
input = sys.stdin.readline


def find(x):
    if x != name[x]:
        name[x] = find(name[x])

    return name[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        name[y] = x
        graph[x] += graph[y]

    print(graph[x])


for _ in range(int(input())):
    f = int(input())
    name = dict()
    graph = dict()

    for _ in range(f):
        a, b = input().split()
        if a not in name:
            name[a] = a
            graph[a] = 1

        if b not in name:
            name[b] = b
            graph[b] = 1

        union(a, b)
