from collections import deque
import sys
input=sys.stdin.readline

d=[[-1,0],[1,0],[0,1],[0,-1]]

# 빙산 덩어리 확인 및 빙산 근처의 바다 개수 기록
def check(start):
    q=deque([start])
    visited[start[0]][start[1]]=1
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m:
                if glaciers[yy][xx]==0:
                    visited[y][x]+=1
                if visited[yy][xx]==0 and glaciers[yy][xx]!=0:
                    visited[yy][xx]=1
                    q.append([yy,xx])
    return

# 입력
n,m=map(int,input().split())
glaciers=[list(map(int,input().split())) for _ in range(n)]
result=0

# 진행
while 1:

    # 빙산 덩어리의 개수
    island=0
    visited=[[0]*m for _ in range(n)]

    # 빙산 확인
    for y in range(n):
        for x in range(m):
            if visited[y][x]==0 and glaciers[y][x]!=0:
                check([y,x])
                island+=1

    # 빙산이 다 녹아서 없으면 종료
    if island==0:
        print(0)
        break

    # 빙산 덩어리가 2개 이상이라면 종료
    if island>1:
        print(result)
        break

    # 빙산 녹음 반영
    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                glaciers[y][x]-=(visited[y][x]-1)
                if glaciers[y][x]<0: glaciers[y][x]=0

    # 연도 지남
    result+=1