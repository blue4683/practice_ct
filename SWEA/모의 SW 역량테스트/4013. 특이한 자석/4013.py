from collections import deque

d=[1,-1]

def rotate(start,dir):
    next=deque([(start,dir)])
    q=deque([(start,dir)])
    visited[start]=1
    while q:
        x,direction=q.popleft()
        for dx in d:
            xx=x+dx
            if 0<=xx<4 and not visited[xx]:
                visited[xx]=1
                if (dx==1 and magnets[x][2]+magnets[xx][6]==1) or (dx==-1 and magnets[x][6]+magnets[xx][2]==1):
                    q.append((xx,-1*direction))
                    next.append((xx,-1*direction))
    while next:
        x,direction=next.popleft()
        magnet=magnets[x]
        if direction==1:
            magnet.appendleft(magnet.pop())
        else:
            magnet.append(magnet.popleft())
        magnets[x]=magnet

for testcase in range(1,int(input())+1):
    k=int(input())
    magnets=[deque(list(map(int,input().split()))) for _ in range(4)]
    result=0
    for _ in range(k):
        idx,dir=map(int,input().split())
        visited=[0]*4
        rotate(idx-1,dir)
    for x in range(4):
        if magnets[x][0]==1:
            result+=(2**x)
    print(f'#{testcase} {result}')