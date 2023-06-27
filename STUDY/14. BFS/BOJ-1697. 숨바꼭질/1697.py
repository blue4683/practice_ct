from collections import *

dx = [-1,1,2]

def hide_and_seek(n):
    q=deque([n])

    while q:
        x=q.popleft()
        for idx in range(len(dx)):
            if idx==2: xx=x*dx[idx]
            else: xx=x+dx[idx]
            
            if 0<=xx<int(1e5+1) and not visited[xx]:
                visited[xx]=visited[x]+1
                if xx==k: return
                q.append(xx)

n,k=map(int,input().split())
visited=[0]*int(1e5+1)
visited[n]=1

hide_and_seek(n)
print(visited[k]-1)