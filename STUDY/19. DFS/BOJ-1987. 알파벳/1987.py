import sys
input=sys.stdin.readline

d=[[-1,0],[1,0],[0,-1],[0,1]]

def index(s):
    return ord(s)-ord('A')

def dfs(depth,y,x):
    global result
    result=max(result,depth)

    for dy,dx in d:
        yy,xx=y+dy,x+dx
        if 0<=yy<r and 0<=xx<c and visited[index(board[yy][xx])]==0:
            visited[index(board[yy][xx])]=1
            dfs(depth+1,yy,xx)
            visited[index(board[yy][xx])]=0

r,c=map(int,input().split())
board=[list(input()) for _ in range(r)]
visited=[0]*(index('Z')+1)
visited[index(board[0][0])]=1
result=0
dfs(1,0,0)
print(result)