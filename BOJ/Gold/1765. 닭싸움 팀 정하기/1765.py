import sys
input = sys.stdin.readline


def find(x):
    if graph[x] != x:
        x = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


n = int(input())
m = int(input())

graph = [i for i in range(n + 1)]
enemy = [[] for _ in range(n + 1)]

for _ in range(m):
    is_friend, a, b = input().split()
    a, b = map(int, [a, b])
    if is_friend == 'F':
        union(a, b)

    else:
        enemy[a].append(b)
        enemy[b].append(a)

for i in range(1, n + 1):
    for j in enemy[i]:
        for k in enemy[j]:
            union(i, k)

result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if find(j) == i:
            result += 1
            break

print(result)
