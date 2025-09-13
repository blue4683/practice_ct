from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = deque(map(int, input().split()))
visited = [0] * (n + 1)
visited[1] = 1
wait = deque([{1}])
while wait:
    q = wait.popleft()
    while q:
        if q and order[0] not in q:
            print(0)
            exit()

        tmp = set()
        x = order.popleft()
        q.discard(x)
        for xx in graph[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            tmp.add(xx)

        if tmp:
            wait.append(tmp)

print(1)
