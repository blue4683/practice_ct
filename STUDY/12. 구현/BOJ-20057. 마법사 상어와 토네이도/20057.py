import sys
input=sys.stdin.readline

# 8방향 정의(서->남서->남->....->북서)
dy=[0,1,1,1,0,-1,-1,-1]
dx=[-1,-1,0,1,1,1,0,-1]

# 흩어지는 모래 계산
def scatter(pos):
    global result
    y,x,dir=pos
    # 진행 방향의 반시계 순으로 퍼센트 정리(거리가 두칸인 경우를 먼저 계산)
    percent=[0.1,0.02,0.07,0.01,0.01,0.02,0.07,0.1,0.05]
    idx=0
    # 토네이도가 있는 곳의 모래 양
    remain=sand[y][x]
    for i in range(1,9):
        # 경로의 반대방향은 흩어지지 않으므로 생략
        if i==4: continue
        # 거리가 두칸이 있는 경우 먼저 계산(방향이 대각선이 아닐 때)
        if i%2==0:
            scattered=int((sand[y][x]*percent[idx])//1)
            remain-=scattered
            yy,xx=y+dy[(dir+i)%8]*2,x+dx[(dir+i)%8]*2
            if 0<=yy<n and 0<=xx<n:
                sand[yy][xx]+=scattered
            else:
                result+=scattered
            idx+=1
        # 거리가 한칸인 경우 계산
        yy,xx=y+dy[(dir+i)%8],x+dx[(dir+i)%8]
        if i==8:
            if 0<=yy<n and 0<=xx<n:
                sand[yy][xx]+=remain
            else:
                result+=remain
        else:
            scattered=int((sand[y][x]*percent[idx])//1)
            remain-=scattered
            if 0<=yy<n and 0<=xx<n:
                sand[yy][xx]+=scattered
            else:
                result+=scattered
            idx+=1
    # 토네이도가 있는 곳의 모래 제거
    sand[y][x]=0
    return

# 토네이도 이동
def tornado(pos):
    y,x,dir=pos
    # 시작지점에서는 패스
    if y==n//2 and x==n//2:
        pass
    # 진행방향 결정(반시계 방향으로 90도 회전했을 때 방문하지 않았다면 경로 변경)
    else:
        yy,xx=y+dy[(dir+2)%8],x+dx[(dir+2)%8]
        if 0<=yy<n and 0<=xx<n and visited[yy][xx]==0:
            dir=(dir+2)%8

    yy,xx=y+dy[dir],x+dx[dir]
    visited[yy][xx]=1
    scatter([yy,xx,dir])
    return [yy,xx,dir]

n=int(input())
sand=[list(map(int,input().split())) for _ in range(n)]

result=0
visited=[[0]*n for _ in range(n)]
visited[n//2][n//2]=1
pos=[n//2,n//2,0]

# 토네이도가 (0,0)에 도달하는 경우 종료
while pos!=[0,0,0]:
    pos=tornado(pos)

print(result)