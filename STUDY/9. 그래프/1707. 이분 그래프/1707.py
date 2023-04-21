from collections import deque
import sys
input=sys.stdin.readline

def bfs(i):
    global bipartite,result
    q=deque([i])
    visited[i]=bipartite
    while q:
        now=q.popleft()
        bipartite=visited[now]*-1
        for node in graph[now]:
            if visited[node]==0:
                visited[node]=bipartite
                q.append(node)
            elif visited[node]+visited[now]:
                result=0
                return
    return

for _ in range(int(input())):
    v,e=map(int,input().split())
    visited=[0]*(v+1)
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        now,next=map(int,input().split())
        graph[now].append(next)
        graph[next].append(now)
    result=1
    bipartite=1
    for i in range(1,v+1):
        if result==0:
            break
        if visited[i]==0:
            bfs(i)
    print('YES') if result else print('NO')