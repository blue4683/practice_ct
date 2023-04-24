from collections import deque

def bfs():
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    answer[now[2]]=1
    while q:
        a,b=q.popleft()
        c=now[2]-(a+b)
        for s,r in cases:
            next=[a,b,c]
            next[r]+=next[s]
            next[s]=0
            if next[r]>now[r]:
                next[s]=next[r]-now[r]
                next[r]=now[r]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]]=1
                q.append((next[0],next[1]))
                if not next[0]:
                    answer[next[2]]=1

now=list(map(int,input().split()))
cases=[[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]
visited=[[0]*201 for _ in range(201)]
answer=[0]*201
bfs()

for i in range(201):
    if answer[i]:
        print(i,end=' ')