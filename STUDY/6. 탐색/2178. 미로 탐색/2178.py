from collections import deque
import sys
input=sys.stdin.readline

def bfs():
    q=deque([(0,0)])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and maze[yy][xx] and not visited[yy][xx]:
                visited[yy][xx]=visited[y][x]+1
                if yy==n-1 and xx==m-1: return visited[yy][xx]
                q.append((yy,xx))

d=[[1,0],[-1,0],[0,1],[0,-1]]
n,m=map(int,input().split())
maze=[list(map(int,list(input().rstrip()))) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
visited[0][0]=1
result=bfs()
print(result)