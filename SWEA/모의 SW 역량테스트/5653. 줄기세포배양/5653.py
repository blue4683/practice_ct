d=[[0,1],[1,0],[-1,0],[0,-1]]

def deactivate(arr,h,w,time):
    for y in range(h):
        for x in range(w):
            if arr[y][x][0]<=0: continue
            if sum(arr[y][x])+arr[y][x][0]==time: arr[y][x]=[-1,-1]
    return arr

def expand(arr,h,w):
    flag=0
    for x in [0,w-1]:
        for y in range(h):
            if arr[y][x][0]: 
                flag=1
                break

    if arr[0]==[[0,0]]*w and arr[h-1]==[[0,0]]*w and not flag:
        return arr,h,w

    for y in range(h):
        arr[y]=[[0,0]]+arr[y]+[[0,0]]
    return [[[0,0]]*(w+2)]+arr+[[[0,0]]*(w+2)],h+2,w+2

def activate(arr,h,w,time):
    visited=[[[0,0]]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if arr[y][x][0]<=0: continue
            if sum(arr[y][x])+1==time:
                for dy,dx in d:
                    yy,xx=y+dy,x+dx
                    if arr[yy][xx][0]: continue
                    if visited[yy][xx][0]<arr[y][x][0]: visited[yy][xx]=[arr[y][x][0],time]
    for y in range(h):
        for x in range(w):
            if visited[y][x][0]: arr[y][x]=visited[y][x]
    return arr

def check(arr,h,w):
    global result
    for y in range(h):
        for x in range(w):
            if arr[y][x][0]<=0: continue
            result+=1

for testcase in range(1,int(input())+1):
    n,m,k=map(int,input().split())
    cells=[list(map(int,input().split())) for _ in range(n)]
    cells=[list(map(lambda x:[x,0], cell)) for cell in cells]
    result=0
    time=0
    while time!=k:
        time+=1
        h,w=len(cells),len(cells[0])
        cells,h,w=expand(cells,h,w)
        cells=activate(cells,h,w,time)
        cells=deactivate(cells,h,w,time)
    check(cells,h,w)
    print(f'#{testcase} {result}')