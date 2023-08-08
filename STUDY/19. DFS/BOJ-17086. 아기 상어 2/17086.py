from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

n,m=map(int,input().split())
sharks=[list(map(int,input().split())) for _ in range(n)]
pos=deque([(y,x) for y in range(n) for x in range(m) if sharks[y][x]])

while pos:
    y,x=pos.popleft()
    for dy,dx in d:
        yy,xx=y+dy,x+dx
        if 0<=yy<n and 0<=xx<m and (sharks[yy][xx]>sharks[y][x]+1 or sharks[yy][xx]==0):
            sharks[yy][xx]=sharks[y][x]+1
            pos.append((yy,xx))

print(max(map(max,sharks))-1)