import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
built = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    indegree[y] += 1
    graph[x].append(y)

for _ in range(k):
    state, a = map(int, input().split())
    if state == 1:
        if indegree[a]:
            print('Lier!')
            exit()

        built[a] += 1
        if built[a] == 1:
            for x in graph[a]:
                indegree[x] -= 1

    else:
        if not built[a]:
            print('Lier!')
            exit()

        built[a] -= 1
        if not built[a]:
            for x in graph[a]:
                indegree[x] += 1

print('King-God-Emperor')
