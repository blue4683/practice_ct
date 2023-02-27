from collections import deque
import sys
input=sys.stdin.readline

dy=[1,-1,0,0]
dx=[0,0,1,-1]

def bfs(pos):
    q=deque(pos)
    while q:
        y,x=q.popleft()
        for i in range(4):
            yy,xx=y+dy[i],x+dx[i]
            if 0<=yy<n and 0<=xx<m and not tomato[yy][xx]:
                tomato[yy][xx]=tomato[y][x]+1
                q.append((yy,xx))

m,n=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(n)]
pos=[]
result=0
for y in range(n):
    for x in range(m):
        if tomato[y][x]==1:
            pos.append((y,x))
if len(pos)==m*n:
    print(0)
    exit()
else:
    bfs(pos)
for y in range(n):
    for x in range(m):
        if not tomato[y][x]:
            print(-1)
            exit()
        if tomato[y][x]>result:
            result=tomato[y][x]
print(result-1)
