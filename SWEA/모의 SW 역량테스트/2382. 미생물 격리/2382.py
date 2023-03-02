from collections import deque

direction=[[],[-1,0],[1,0],[0,-1],[0,1]]
change_direction={1:2,2:1,3:4,4:3}
def move(micro):
    q=deque(micro)
    tmp=[]
    while q:
        y,x,v,d=q.popleft()
        dy,dx=direction[d]
        yy,xx=y+dy,x+dx
        if 0<=yy<n and 0<=xx<n:
            if not yy or not xx or yy==n-1 or xx==n-1:
                v//=2
                d=change_direction[d]
            if not sector[yy][xx]:
                sector[yy][xx]=[[v,d]]
            else:
                sector[yy][xx]+=[[v,d]]
    for y in range(n):
        for x in range(n):
            if not sector[y][x]: continue
            if len(sector[y][x])>=1:
                max_v=max(sector[y][x],key=lambda x:x[0])[0]
                for v,d in sector[y][x]:
                    if v==max_v:
                        change_d=d
                sum_v=sum(list(map(lambda x:x[0],sector[y][x])))
                tmp.append([y,x,sum_v,change_d])
                sector[y][x]=0
    return tmp

for testcase in range(1,int(input())+1):
    n,m,k=map(int,input().split())
    micro=[list(map(int,input().split())) for _ in range(k)]
    sector=[[0]*n for _ in range(n)]
    for _ in range(m):
        micro=move(micro)
    result=sum(list(map(lambda x:x[2],micro)))
    print(f'#{testcase} {result}')