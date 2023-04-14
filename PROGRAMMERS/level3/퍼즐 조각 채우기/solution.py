from collections import deque

d=[(1,0),(0,1),(-1,0),(0,-1)]

def normalize(pos):
    n_pos=[]
    min_y,min_x=51,51
    max_y,max_x=0,0
    for y,x in pos:
        min_y,min_x=min(min_y,y),min(min_x,x)
        max_y,max_x=max(max_y,y),max(max_x,x)
    n_pos=list(map(lambda x:[x[0]-min_y,x[1]-min_x],pos))
    max_y-=min_y
    max_x-=min_x
    arr=[[0]*(max_x+1) for _ in range(max_y+1)]
    for y,x in n_pos:
        arr[y][x]=1
    return arr

def rotate_arr(arr):
    b,a=len(arr),len(arr[0])
    rotated_arr=[]
    for x in range(a):
        rotated_arr+=[[arr[y][x] for y in range(b-1,-1,-1)]]
    return rotated_arr

def bfs(graph,start,flag,n):
    pos=[]
    q=deque([start])
    while q:
        y,x=q.popleft()
        pos+=[[y,x]]
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<n and 0<=xx<n and graph[yy][xx]==flag:
                graph[yy][xx]=not flag
                q+=[[yy,xx]]
    arr=normalize(pos)
    return graph,arr

def find(graph,flag,n):
    arr=[]
    for y in range(n):
        for x in range(n):
            if graph[y][x]==flag:
                graph[y][x]=not flag
                graph,res=bfs(graph,[y,x],flag,n)
                arr+=[res]
    return arr

def match(hole,block):
    for _ in range(4):
        if hole==block:
            return sum(list(map(sum,block)))
        block=rotate_arr(block)
    return 0

def solution(game_board, table):
    answer = 0
    n=len(game_board)
    holes,blocks=find(game_board,0,n),find(table,1,n)
    b=len(blocks)
    visited=[0]*(b+1)
    for hole in holes:
        for i in range(b):
            if not visited[i]:
                block=blocks[i]
                cnt=match(hole,block)
                if cnt:
                    visited[i]=1
                    answer+=cnt
                    break
    return answer