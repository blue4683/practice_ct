import sys
input=sys.stdin.readline

# 방향
d=[[-1,0],[0,1],[1,0],[0,-1]]

# 로봇 청소기 작동
def search(pos):
    global result

    y,x,dir=pos

    # 1번 수행
    if room[y][x]==0:
        room[y][x]=2
        result+=1

    # 3번 수행
    for i in range(1,5):
        new_dir=(dir+4-i)%4
        dy,dx=d[new_dir]
        yy,xx=y+dy,x+dx
        if 0<=yy<n and 0<=xx<m and room[yy][xx]==0:
            next=[yy,xx,new_dir]
            break

    # 주변이 모두 청소되어 있다면 2번 수행
    else:
        dy,dx=d[(dir+2)%4]
        yy,xx=y+dy,x+dx
        next=[yy,xx,dir] if (0<=yy<n and 0<=xx<m and room[yy][xx]!=1) else 0

    # 이동한 좌표 반환
    return next

# 입력 및 기본 값 정의
n,m=map(int,input().split())
pos=list(map(int,input().split()))
room=[list(map(int,input().split())) for _ in range(n)]
result=0

# 수행
while pos:
    pos=search(pos)

# 결과
print(result)