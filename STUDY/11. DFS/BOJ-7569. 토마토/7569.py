from collections import deque
import sys
input=sys.stdin.readline

d=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def bfs(pos):
    q=deque(pos)
    while q:
        z,y,x=q.popleft()
        for dz,dy,dx in d:
            zz,yy,xx=z+dz,y+dy,x+dx
            if 0<=zz<h and 0<=yy<n and 0<=xx<m and tomatoes[zz][yy][xx]==0:
                tomatoes[zz][yy][xx]=tomatoes[z][y][x]+1
                q.append((zz,yy,xx))

    result=0

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x]==0:
                    return -1
                else:
                    result=max(result,tomatoes[z][y][x]-1)

    return result

m,n,h=map(int,input().split())
tomatoes=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
pos=[]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x]==1:
                pos.append((z,y,x))

print(bfs(pos))