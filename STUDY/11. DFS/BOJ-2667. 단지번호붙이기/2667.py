from collections import deque
import sys
input=sys.stdin.readline

d=[(1,0),(0,1),(-1,0),(0,-1)]

def numbering(sy,sx):
    cnt=0
    q=deque([(sy,sx)])
    homes[sy][sx]=0
    while q:
        y,x=q.popleft()
        cnt+=1
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<n and homes[yy][xx]:
                homes[yy][xx]=0
                q.append((yy,xx))
    
    return cnt

n=int(input())
homes=[list(map(int,list(input().strip()))) for _ in range(n)]
address=[]

for y in range(n):
    for x in range(n):
        if homes[y][x]:
            address.append(numbering(y,x))

print(len(address))
for add in sorted(address):
    print(add) 