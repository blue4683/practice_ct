from queue import PriorityQueue
import sys
input=sys.stdin.readline

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a>b: graph[a]=b
    else: graph[b]=a

n=int(input())
arr=[list(input().strip()) for _ in range(n)]

edges=PriorityQueue()
for y in range(n):
    for x in range(n):
        v=arr[y][x]
        if v=='0':
            arr[y][x]=0
            continue
        elif v.islower(): arr[y][x]=ord(v)-ord('a')+1
        else: arr[y][x]=27+ord(v)-ord('A')
        if x==y: continue
        edges.put([arr[y][x],y,x])

graph=[i for i in range(n)]
answer=sum(map(lambda x:sum(x),arr))
while edges.qsize()>0:
    l,s,e=edges.get()
    if find(s)!=find(e):
        union(s,e)
        answer-=l
        n-=1

print(answer) if n==1 else print(-1)