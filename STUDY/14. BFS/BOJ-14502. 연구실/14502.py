from collections import deque
import sys
input=sys.stdin.readline

d=[[1,0],[0,1],[-1,0],[0,-1]]

def copy_arr(arr):
    new_arr=[]
    for l in arr:
        new_arr.append(l[:])
    return new_arr

def build_wall(depth,arr):
    global result
    if depth==3:
        result=max(result,simulate(pos,copy_arr(arr)))
        return
    
    for y in range(n):
        for x in range(m):
            if 0<=y<n and 0<=x<m and arr[y][x]==0:
                arr[y][x]=1
                build_wall(depth+1,arr)
                arr[y][x]=0
    
def simulate(pos,arr):
    global result
    q=deque(pos)
    cnt=safe+len(pos)

    while q:
        y,x=q.popleft()
        cnt-=1
        if cnt<=result: return 0
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<m and arr[yy][xx]==0:
                arr[yy][xx]=2
                q.append((yy,xx))
    
    return cnt

n,m=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(n)]
pos=[(y,x) for y in range(n) for x in range(m) if lab[y][x]==2]
safe=sum(list(map(lambda x:x.count(0),lab)))-3
result=0

build_wall(0,lab)
print(result)