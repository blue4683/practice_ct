import sys
input=sys.stdin.readline

def dfs(depth,p):
    global result
    if depth==4:
        result=1
        return
    visited[p]=1
    for i in arr[p]:
        if not visited[i]:
            dfs(depth+1,i)
    visited[p]=0

n,m=map(int,input().split())
arr=[[] for _ in range(n+1)]
visited=[0]*(n+1)
result=0
for _ in range(m):
    y,x=map(int,input().split())
    arr[y]+=[x]
    arr[x]+=[y]
for node in range(n):
    dfs(0,node)
    if result:
        break
print(result)