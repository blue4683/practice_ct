import sys
input=sys.stdin.readline
INF=10000
MIN=INF

n,m=map(int,input().split())
relations=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    relations[i][i]=0
for _ in range(m):
    a,b=map(int,input().split())
    relations[a][b]=1
    relations[b][a]=1

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if relations[start][end]>relations[start][mid]+relations[mid][end]:
                relations[start][end]=relations[start][mid]+relations[mid][end]

result=list(map(lambda x:sum(x[1:]),relations))
print(result.index(min(result)))