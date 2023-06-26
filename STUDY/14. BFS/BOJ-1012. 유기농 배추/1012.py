from collections import *
import sys
input = sys.stdin.readline

def bfs(pos):
    global cnt
    if lawn[pos[0]][pos[1]] == 0:
        return
    lawn[pos[0]][pos[1]] = 0
    q = deque([pos])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        y,x = q.popleft()
        for idx in range(len(dx)):
            yy = y+dy[idx]
            xx = x+dx[idx]
            if 0<=yy<n and 0<=xx<m and lawn[yy][xx]:
                lawn[yy][xx] = 0
                q.append((yy,xx))
    cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    lawn = [[0]*(m+1) for _ in range(n)]
    pos = []
    cnt = 0
    for _ in range(k):
        x,y = map(int, input().split())
        lawn[y][x]=1
        pos.append((y,x))
    for p in pos:   
        bfs(p)
    print(cnt)