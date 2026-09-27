from collections import deque


n = int(input())
if n == 1:
    for _ in range(2):
        print(1)
        
else:
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
        
    q = deque([x for x in range(1, n + 1) if degree[x] == 1])
    removed = [0] * (n + 1)
    remain = n
    while remain > 2:
        k = len(q)
        remain -= k
        for _ in range(k):
            x = q.popleft()
            removed[x] = 1
            for xx in graph[x]:
                if removed[xx]:
                    continue
                
                degree[xx] -= 1
                if degree[xx] == 1:
                    q.append(xx)
                    
    print(len(q))
    print(*sorted(q))
