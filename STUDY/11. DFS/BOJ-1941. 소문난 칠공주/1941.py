from collections import deque

d=[(1,0),(0,1),(-1,0),(0,-1)]

def link(arr):
    visited=[[0]*5 for _ in range(5)]
    for y,x in arr:
        visited[y][x]=1
    q=deque([arr[0]])
    while q:
        y,x=q.popleft()
        visited[y][x]=0
        for dy,dx in d:
            yy,xx=y+dy,x+dx
            if 0<=yy<5 and 0<=xx<5 and visited[yy][xx]==1:
                q.append((yy,xx))
    return sum(list(map(sum,visited)))

def dfs(depth,start,visited,count):
    global result
    if count>=4: return
    if depth==7:
        flag=link(visited)
        if flag==0: result+=1
        return

    for i in range(start,25):
        dfs(depth+1,i+1,visited+[(i//5,i%5)],count+int(cases[i]=='Y'))

students=[list(input()) for _ in range(5)]
cases=[]
for student in students:
    cases.extend(student)
result=0
dfs(0,0,[],0)
print(result)