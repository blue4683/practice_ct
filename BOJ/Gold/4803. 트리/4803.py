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


t = 0
while 1:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    t += 1
    graph = [i for i in range(n + 1)]
    cycle_node = set()
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)

        else:
            cycle_node.add(a)

    for i in range(n + 1):
        find(i)

    exceptions = set()
    for node in cycle_node:
        exceptions.add(find(node))

    trees = set(graph) - exceptions
    result = len(trees) - 1
    if result > 1:
        print(f'Case {t}: A forest of {result} trees.')

    elif result == 1:
        print(f'Case {t}: There is one tree.')

    else:
        print(f'Case {t}: No trees.')
