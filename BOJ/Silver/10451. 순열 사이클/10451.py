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


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [i for i in range(n + 1)]
    result = 0
    for i in range(n):
        if find(i + 1) == find(arr[i]):
            result += 1
            continue

        union(i + 1, arr[i])

    print(result)
