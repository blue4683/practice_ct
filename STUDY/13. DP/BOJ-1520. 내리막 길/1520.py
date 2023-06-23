import sys
sys.setrecursionlimit(int(1e9))
input=sys.stdin.readline

d=[[0,1],[0,-1],[-1,0],[1,0]]

def find(y,x):
    if (y,x)==(m-1,n-1):
        return 1
    
    if result[y][x]!=-1:
        return result[y][x]
    
    result[y][x]=0

    for dy,dx in d:
        yy,xx=y+dy,x+dx
        if 0<=yy<m and 0<=xx<n and road[yy][xx]<road[y][x]:
            result[y][x]+=find(yy,xx)
    
    return result[y][x]

m,n=map(int,input().split())
road=[list(map(int,input().split())) for _ in range(m)]
result=[[-1]*n for _ in range(m)]

print(find(0,0))