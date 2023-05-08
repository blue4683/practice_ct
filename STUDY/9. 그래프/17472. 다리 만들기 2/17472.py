from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs(start,index):
    global visited,pos
    visited[start[0]][start[1]]=1
    q=deque([start])
    while q:
        y,x=q.popleft()
        pos.append([y,x,index])
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and arr[yy][xx] and not visited[yy][xx]:
                visited[yy][xx]=1
                q.append((yy,xx))

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a>b: graph[a]=b
    else: graph[b]=a

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

pos=[]
index=1
for y in range(n):
    for x in range(m):
        if arr[y][x] and not visited[y][x]:
            bfs((y,x),index)
            index+=1

graph=[i for i in range(index)]
edges=[]
for y,x,i in pos:
    for yy,xx,ii in pos:
        if i==ii: continue
        if y!=yy and x!=xx: continue
        flag=0
        if x==xx:
            s,e=(y,yy) if y<yy else (yy,y)
            for yyy in range(s+1,e):
                if arr[yyy][x]: flag=1
        else:
            s,e=(x,xx) if x<xx else (xx,x)
            for xxx in range(s+1,e):
                if arr[y][xxx]: flag=1
        if flag: continue
        cost=e-s-1
        if cost>1:
            edges.append([i,ii,cost])
edges.sort(key=lambda x:x[-1])

answer=0
for s,e,cost in edges:
    if find(s)!=find(e):
        union(s,e)
        answer+=cost
        index-=1

print(answer) if index==2 else print(-1)