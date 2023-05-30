from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e9))

d=[(1,0),(0,1),(-1,0),(0,-1)]

def flooding(arr,rf):
    new_arr=[]
    for y in range(n):
        new_arr.append(list(map(lambda x:x if x>rf else 0,arr[y])))
    return new_arr

def find(start):
    sy,sx=start
    flooded[sy][sx]=0
    q=deque([start])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<n and flooded[yy][xx]:
                flooded[yy][xx]=0
                q.append((yy,xx))

# def find(start):
#     y,x=start
#     for dy,dx in d:
#         yy,xx=y+dy,x+dx
#         if 0<=yy<n and 0<=xx<n and flooded[yy][xx]:
#             flooded[yy][xx]=0
#             find((yy,xx))

n=int(input())
section=[list(map(int,input().split())) for _ in range(n)]
MAX=max(list(map(lambda x:max(x),section)))
result=1
rf=1
while rf<MAX:
    flooded=flooding(section,rf)
    safe_zone=0
    for y in range(n):
        for x in range(n):
            if flooded[y][x]:
                safe_zone+=1
                find((y,x))
    result=max(result,safe_zone)
    rf+=1

print(result)