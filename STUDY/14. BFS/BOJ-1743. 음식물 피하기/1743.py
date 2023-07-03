from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1]]

def find(p):
    sy,sx=p
    size=1
    foods[sy][sx]=0
    q=deque([p])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and foods[yy][xx]==1:
                foods[yy][xx]=0
                size+=1
                q.append((yy,xx))

    return size

n,m,k=map(int,input().split())
foods=[[0]*m for _ in range(n)]
pos=[]
result=0
for _ in range(k):
    y,x=map(lambda x:int(x)-1,input().split())
    foods[y][x]=1
    pos.append((y,x))

for p in pos: result=max(result,find(p))
print(result)