def dfs(depth,y,x,honey):
    global max_honey
    if sum(honey)>c:
        return
    if depth==m:
        tmp=sum(list(map(lambda x:x**2,honey)))
        max_honey=max(max_honey,tmp)
        return
    dfs(depth+1,y,x,honey+[hive[y][x+depth]])
    dfs(depth+1,y,x,honey)

def find(depth,y,x,honey):
    global result
    if depth==2:
        result=max(result,honey)
        return
    for yy in range(n):
        for xx in range(n-m+1):
            if yy==y and x-m<xx<x+m: continue
            if not visited[yy][xx]:
                for i in range(m):
                    visited[yy][xx+i]=1
                find(depth+1,yy,xx,honey+harvest[yy][xx])
                for i in range(m):
                    visited[yy][xx+i]=0

for testcase in range(1,int(input())+1):
    n,m,c=map(int,input().split())
    hive=[list(map(int,input().split())) for _ in range(n)]
    harvest=[[0]*n for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    result=0
    for y in range(n):
        for x in range(n-m+1):
            max_honey=0
            dfs(0,y,x,[])
            harvest[y][x]=max_honey
    find(0,0,0,0)
    print(f'#{testcase} {result}')