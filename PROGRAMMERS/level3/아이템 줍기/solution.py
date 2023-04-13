from collections import deque

d=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(start,graph,itemX,itemY):
    q=deque([start])
    while q:
        y,x=q.popleft()
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<101 and 0<=xx<101 and graph[yy][xx]>graph[y][x]+1:
                graph[yy][xx]=graph[y][x]+1
                if yy==itemY and xx==itemX:
                    return graph[yy][xx]
                q+=[(yy,xx)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph=[[-1]*102 for _ in range(101)]
    for info in rectangle:
        x1,y1,x2,y2=map(lambda x:x*2,info)
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if (y in [y1,y2] or x in [x1,x2]) and graph[y][x]!=-2:
                    graph[y][x]=1e9
                else:
                    graph[y][x]=-2
    graph[characterY*2][characterX*2]=0
    answer=bfs((characterY*2,characterX*2),graph,itemX*2,itemY*2)//2
    return answer