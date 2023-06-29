from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1]]

def find_border(arr):
    global time
    arr[0][0]=time
    q=deque([(0,0)])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and time<arr[yy][xx]<1:
                arr[yy][xx]=time
                q.append((yy,xx))

    return arr

def find_cheese(arr):
    return [(y,x) for y in range(n) for x in range(m) if arr[y][x]==1]

def melt(arr,pos):
    global time
    melted=[]
    remained=[]
    q=deque(pos)
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and arr[yy][xx]==time:
                melted.append((y,x))
                break
        else: remained.append((y,x))

    for y,x in melted: arr[y][x]=-1
    return arr,remained

time=0
n,m=map(int,input().split())
cheese=[list(map(int,input().split())) for _ in range(n)]
pos=find_cheese(cheese)
pieces=0

while pos:
    time-=1
    pieces=len(pos)
    cheese,pos=melt(find_border(cheese),pos)

print(-time)
print(pieces)