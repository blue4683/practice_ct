import sys
input=sys.stdin.readline

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a==b: return
    if a>b: graph[a]=b
    else: graph[b]=a


n=int(input())
m=int(input())
info=[list(map(int,input().split())) for _ in range(n)]
dest=sorted(list(map(int,input().split())))
graph=[i for i in range(n)]
for y in range(n):
    for x in range(n):
        if info[y][x]:
            union(y,x)
for city in dest:
    if graph[city-1]!=dest[0]-1:
        print('NO')
        break
else:
    print('YES')