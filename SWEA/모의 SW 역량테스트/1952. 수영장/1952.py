def dfs(depth,cost):
    global result
    if cost>=result: return
    if depth>=12:
        if cost<result:
            result=cost
        return
    if not plan[depth]: dfs(depth+1,cost)
    else:
        d1,m1,m3,_=ticket
        dfs(depth+1,cost+d1*plan[depth])
        dfs(depth+1,cost+m1)
        dfs(depth+3,cost+m3)

for testcase in range(1,int(input())+1):
    ticket=list(map(int,input().split()))
    plan=list(map(int,input().split()))
    result=ticket[-1]
    dfs(0,0)
    print(f'#{testcase} {result}')