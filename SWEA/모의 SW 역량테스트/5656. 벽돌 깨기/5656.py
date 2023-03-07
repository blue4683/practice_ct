from collections import deque

d=[[1,0],[0,1],[-1,0],[0,-1]]

def copy_brick(arr):
    new_arr=[]
    for x in range(w):
        new_arr+=[arr[x][:]]
    return new_arr

def shoot(depth,brick):
    global result
    if brick==[[0]*h for _ in range(w)]:
        result=0
        return
    if depth==n:
        res=0
        for x in range(w):
            res+=sum(map(bool,brick[x]))
        result=min(res,result)
        return
    for x in range(w):
        for y in range(h):
            if brick[x][y]:
                tmp=copy_brick(brick)
                shoot(depth+1,crack([x,y],tmp[x][y],tmp,[[0]*h for _ in range(w)]))
                break

def crack(start,power,arr,check):
    a,b=start
    check[a][b]=1
    q=deque([start+[power]])
    while q:
        x,y,p=q.popleft()
        if p==1:continue
        for k in range(p):
            for dx,dy in d:
                xx,yy=x+dx*k,y+dy*k
                if 0<=xx<w and 0<=yy<h and not check[xx][yy] and arr[xx][yy]:
                    check[xx][yy]=1
                    if arr[xx][yy]!=1: q.append([xx,yy,arr[xx][yy]])
    for x in range(w):
        for y in range(h):
            if check[x][y]:
                arr[x][y]=0
    # for x in range(w):
    # q=deque(arr[x])
    # while 0 in q:
    #     v=q.popleft()
    #     if not v: continue
    #     q.append(v)
    # while len(q)<h:
    #     q.appendleft(0)
    # arr[x]=list(q)
    # return arr
    new_arr=[]
    for x in range(w):
        tmp=[]
        for y in range(h):
            if arr[x][y]:
                tmp+=[arr[x][y]]
        if len(tmp)<h:
            tmp=[0]*(h-len(tmp))+tmp
        new_arr+=[tmp]
    return new_arr

for testcase in range(1,int(input())+1):
    n,w,h=map(int,input().split())
    bricks=[list(map(int,input().split())) for _ in range(h)]
    bricks=list(map(list,zip(*bricks)))
    result=0
    for x in range(w):
        result+=sum(map(bool,bricks[x]))
    shoot(0,bricks)
    print(f'#{testcase} {result}')