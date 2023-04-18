import sys
input=sys.stdin.readline

def GCD(a,b):
    if not b:
        return a
    return GCD(b,a%b)

def dfs(depth):
    visited[depth]=1
    for rate in rates[depth]:
        next=rate[0]
        if not visited[next]:
            result[next]=result[depth]*rate[2]//rate[1]
            dfs(next)

n=int(input())
rates=[[] for _ in range(n)]
LCM=1
visited=[0]*n
result=[0]*n
for _ in range(n-1):
    a,b,p,q=map(int,input().split())
    rates[a]+=[[b,p,q]]
    rates[b]+=[[a,q,p]]
    LCM*=p*q//GCD(p,q)
result[0]=LCM
dfs(0)
r=result[0]
for i in range(1,n):
    r=GCD(r,result[i])

for i in range(n):
    print(result[i]//r,end=' ')