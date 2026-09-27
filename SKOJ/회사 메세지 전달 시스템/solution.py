from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(s):
    dist = {s: 0}
    q = deque([s])
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if xx in dist:
                continue
            
            dist[xx] = dist[x] + 1
            q.append(xx)
                
    return dist


INF = 10 ** 9
n, m = map(int, input().split())
names = [input().rstrip() for _ in range(n)]

graph = defaultdict(list)    
for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)
    
cache = {}
results = []
for _ in range(int(input())):
    s, e = input().split()
    if s in cache:
        result = cache[s].get(e, -1)
        
    elif e in cache:
        result = cache[e].get(s, -1)
        
    else:
        cache[s] = bfs(s)
        result = cache[s].get(e, -1)
        
    results.append(result)

print('\n'.join(map(str, results)))
