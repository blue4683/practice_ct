import sys
input=sys.stdin.readline

def dfs(depth,eggs,visited):
    global result
    if depth==n or visited.count(0)==1:
        result=max(result,sum(visited))
        return
    d1,w1=eggs[depth]
    if d1<=0:
        dfs(depth+1,eggs,visited)
    else:
        flag1,flag2=0,0
        for i in range(n):
            if i==depth: continue
            if not visited[i]:
                d2,w2=eggs[i]
                td1,td2=d1-w2,d2-w1

                if td1<=0:
                    flag1=1
                    visited[depth]=1
                if td2<=0:
                    flag2=1
                    visited[i]=1

                eggs[depth]=[td1,w1]
                eggs[i]=[td2,w2]
                dfs(depth+1,eggs,visited)

                eggs[depth]=[d1,w1]
                eggs[i]=[d2,w2]

                if flag1:
                    visited[depth]=0
                if flag2:
                    visited[i]=0

n=int(input())
eggs=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n
result=0
dfs(0,eggs,visited)
print(result)