from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

def find(sy,sx):
    q=deque([(sy,sx)])
    mountain[sy][sx]*=-1
    flag=1

    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m:
                if abs(mountain[yy][xx])>abs(mountain[y][x]): flag=0
                if mountain[yy][xx]==abs(mountain[y][x]):
                    mountain[yy][xx]*=-1
                    q.append((yy,xx))
    return flag

n,m=map(int,input().split())
mountain=[list(map(int,input().split())) for _ in range(n)]
result=0

for y in range(n):
    for x in range(m):
        if mountain[y][x]>0: 
            result+=find(y,x)

print(result)