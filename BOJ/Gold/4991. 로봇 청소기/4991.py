from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs(start,i):
    global num
    visited=[[0]*w for _ in range(h)]
    visited[start[0]][start[1]]=1
    q=deque([start])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<h and 0<=xx<w and room[yy][xx]!='x' and visited[yy][xx]==0:
                visited[yy][xx]=visited[y][x]+1
                if room[yy][xx]=='*':
                    graph[i][target.index([yy,xx])]=visited[y][x]
                q.append([yy,xx])

def dfs(depth,now,cost):
    global answer
    if cost>=answer: return
    if depth==num:
        answer=min(answer,cost)
    for i in range(num+1):
        if i!=now and graph[now][i]!=0 and visited[i]==0:
            visited[i]=1
            dfs(depth+1,i,cost+graph[now][i])
            visited[i]=0

while 1:
    w,h=map(int,input().split())
    if w==0 and h==0: break
    room=[list(input().strip()) for _ in range(h)]
    target=[]
    num=0
    for y in range(h):
        for x in range(w):
            if room[y][x]=='o':
                start=[y,x]
            if room[y][x]=='*':
                target.append([y,x])
                num+=1
    target=[start]+target
    graph=[[0]*(num+1) for _ in range(num+1)]
    for i in range(num+1):
        bfs(target[i],i)
    visited=[0]*(num+1)
    answer=1e9
    visited[0]=1
    dfs(0,0,0)
    print(-1) if answer==1e9 else print(answer)