from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    order = [[0] * 2 for _ in range(m + 1)]
    for i in range(1, m + 1):
        if not indegree[i]:
            q.append(i)
            order[i][0] = 1

    while q:
        x = q.popleft()
        for xx in graph[x]:
            if not indegree[xx]:
                continue

            indegree[xx] -= 1
            if order[xx][0] < order[x][0]:
                order[xx] = [order[x][0], 0]

            elif order[xx][0] == order[x][0]:
                order[xx][1] = 1

            if not indegree[xx]:
                q.append(xx)
                if order[xx][1]:
                    order[xx][0] += 1

    print(k, max([order[i][0] for i in range(1, m + 1)]))
