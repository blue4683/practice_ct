d=[[1,0],[-1,0],[0,1],[0,-1]]

def find(depth,y,x,now_h,dig_cnt):
    global result
    for dy,dx in d:
        yy,xx=y+dy,x+dx
        if 0<=yy<n and 0<=xx<n and not visited[yy][xx]:
            go_h=arr[yy][xx]
            if not dig_cnt and go_h>=now_h: continue
            if go_h-k>=now_h: continue
            visited[yy][xx]=1
            if go_h>=now_h:
                find(depth+1,yy,xx,now_h-1,0)
            else:
                find(depth+1,yy,xx,go_h,dig_cnt)
            visited[yy][xx]=0
        else: result=max(result,depth)

for testcase in range(1,int(input())+1):
    n,k=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    max_h=max(map(max,arr))
    result=1
    pos=[]
    for y in range(n):
        for x in range(n):
            if arr[y][x]==max_h:
                pos+=[[y,x]]
    for y,x in pos:
        visited=[[0]*n for _ in range(n)]
        visited[y][x]=1
        find(1,y,x,max_h,1)
    print(f'#{testcase} {result}')

# 2차
# d=[[1,0],[-1,0],[0,1],[0,-1]]

# def find(depth,y,x,now_h,dig_cnt):
#     global result
#     for dy,dx in d:
#         yy,xx=y+dy,x+dx
#         if 0<=yy<n and 0<=xx<n and not visited[yy][xx]:
#             go_h=arr[yy][xx]
#             if not dig_cnt and go_h>=now_h: continue
#             if go_h-k>=now_h: continue
#             if go_h>=now_h:
#                 dig_cnt=0
#                 go_h=now_h-1
#             visited[yy][xx]=1
#             find(depth+1,yy,xx,go_h,dig_cnt)
#             visited[yy][xx]=0
#         else: result=max(result,depth)

# for testcase in range(1,int(input())+1):
#     n,k=map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     max_h=max(map(max,arr))
#     result=1
#     pos=[]
#     for y in range(n):
#         for x in range(n):
#             if arr[y][x]==max_h:
#                 pos+=[[y,x]]
#     for y,x in pos:
#         visited=[[0]*n for _ in range(n)]
#         visited[y][x]=1
#         find(1,y,x,max_h,1)
#     print(f'#{testcase} {result}')

# 1차
# d=[[1,0],[0,1],[-1,0],[0,-1]]

# def dfs(depth,y,x,height,dig):
#     global result
#     result=max(result,depth)
#     for dy,dx in d:
#         yy,xx=y+dy,x+dx
#         if 0<=yy<n and 0<=xx<n and not visited[yy][xx]:
#             h=arr[yy][xx]
#             if h>=height:
#                 dif=h-height+1
#                 if dig<dif: continue
#                 visited[yy][xx]=1
#                 dfs(depth+1,yy,xx,h-dig,0)
#             else:
#                 visited[yy][xx]=1
#                 dfs(depth+1,yy,xx,h,dig)
#             visited[yy][xx]=0

# for testcase in range(1,int(input())+1):
#     n,k=map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     max_height=max(map(max,arr))
#     result=1
#     pos=[]
#     for y in range(n):
#         for x in range(n):
#             if arr[y][x]==max_height:
#                 pos+=[[y,x]]
#     for y,x in pos:
#         visited=[[0]*n for _ in range(n)]
#         visited[y][x]=1
#         dfs(1,y,x,arr[y][x],k)
#     print(f'#{testcase} {result}')