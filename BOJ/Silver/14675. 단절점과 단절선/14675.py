import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 2:
        print('yes')

    else:
        print('yes') if len(graph[k]) > 1 else print('no')
