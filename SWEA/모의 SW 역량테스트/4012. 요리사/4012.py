def dfs(depth,st):
    global taste
    if depth==n//2:
        a,b=0,0
        for y in range(n):
            for x in range(n):
                if not visited[y] and not visited[x]:
                    a+=food[y][x]
                if visited[y] and visited[x]:
                    b+=food[y][x]
        taste=min(taste,abs(a-b))
        return
    
    for i in range(st,n):
        if not visited[i]:
            visited[i]=1
            dfs(depth+1,i)
            visited[i]=0

for testcase in range(1,int(input())+1):
    n=int(input())
    food=[list(map(int,input().split())) for _ in range(n)]
    visited=[0]*n
    taste=1e9
    dfs(0,0)
    print(f'#{testcase} {taste}')