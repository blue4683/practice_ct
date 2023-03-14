import sys
input=sys.stdin.readline

d=[[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    global result
    q=set([(0,0,board[0][0])])
    while q:
        y,x,path=q.pop()
        result=max(result,len(path))
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<r and 0<=xx<c and board[yy][xx] not in path:
                q.add((yy,xx,path+board[yy][xx]))

r,c=map(int,input().split())
board=[list(input().rstrip()) for _ in range(r)]
result=0
bfs()
print(result)

# 1차
# def dfs(depth,y,x,path):
#     global result
#     result=max(result,depth)

#     for dy,dx in d:
#         yy,xx=y+dy,x+dx
#         if 0<=yy<r and 0<=xx<c and board[yy][xx] not in path:
#             path+=[board[yy][xx]]
#             dfs(depth+1,yy,xx,path)
#             path.pop()

# r,c=map(int,input().split())
# board=[list(input()) for _ in range(r)]
# result=0
# dfs(1,0,0,[board[0][0]])
# print(result)