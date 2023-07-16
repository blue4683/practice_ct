from collections import deque
import sys
input=sys.stdin.readline
INF=21e8

d=[[1,0],[0,1],[-1,0],[0,-1]]

def find_cost():
    q=deque([[0,0]])

    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<n:
                cost=visited[y][x]+cave[yy][xx]
                if cost<visited[yy][xx]:
                    visited[yy][xx]=cost
                    q.append([yy,xx])

    return visited[n-1][n-1]

T=0
while 1:
    n=int(input())
    if n==0: break
    T+=1

    cave=[list(map(int,input().split())) for _ in range(n)]
    visited=[[INF]*n for _ in range(n)]
    visited[0][0]=cave[0][0]
    print(f'Problem {T}: {find_cost()}')