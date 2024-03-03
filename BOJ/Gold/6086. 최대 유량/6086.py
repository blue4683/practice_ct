from collections import deque
import sys
input = sys.stdin.readline


def alphabet_to_number(text):
    if text <= 'Z':
        return ord(text) - ord('A')

    return ord(text) - ord('a') + 26


def make_flow(s, t, path):
    c = 10 ** 9
    now = t
    while now != s:
        c = min(c, capacity[path[now]][now] - flow[path[now]][now])
        now = path[now]

    now = t
    while now != s:
        flow[path[now]][now] += c
        flow[now][path[now]] -= c
        now = path[now]

    return c


def bfs(s, t):
    path = [-1] * 52
    q = deque([s])

    while q:
        u = q.popleft()
        for v in graph[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] < 0:
                q.append(v)
                path[v] = u
                if v == t:
                    return make_flow(s, t, path)

    return 0


def edmonds_karp(s, t):
    max_flow = 0
    while 1:
        c = bfs(s, t)
        if c > 0:
            max_flow += c
        else:
            break

    return max_flow


n = int(input())
flow = [[0] * 52 for _ in range(52)]
capacity = [[0] * 52 for _ in range(52)]
graph = [[] for _ in range(52)]

for _ in range(n):
    u, v, c = input().split()
    u, v, c = alphabet_to_number(u), alphabet_to_number(v), int(c)

    graph[u].append(v)
    graph[v].append(u)

    capacity[u][v] += c
    capacity[v][u] += c

result = edmonds_karp(0, 25)
print(result)
