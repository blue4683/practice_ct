from collections import deque
import sys
input=sys.stdin.readline

def bfs(start):
    q=deque([start])
    visited[start]=1
    while q:
        now=q.popleft()
        for next,distance in graph[now]:
            if not visited[next]:
                visited[next]=visited[now]+distance
                q.append(next)

v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v):
    node,*info=list(map(int,input().split()))
    n,d=info[:-1:2],info[1::2]
    for next,distance in zip(n,d):
        graph[node]+=[(next,distance)]
visited=[0]*(v+1)
bfs(1)
max_node=1
for node in range(1,v+1):
    if visited[node]>visited[max_node]:
        max_node=node
visited=[0]*(v+1)
bfs(max_node)
result=max(visited)-1
print(result)

# from collections import deque
# import sys
# input=sys.stdin.readline

# def bfs(start):
#     q=deque([start])
#     visited[start]=1
#     while q:
#         now=q.popleft()
#         for next,distance in graph[now]:
#             if not visited[next]:
#                 visited[next]=visited[now]+distance
#                 q.append(next)

# v=int(input())
# graph=[[] for _ in range(v+1)]
# result=0
# for _ in range(v):
#     node,*info=list(map(int,input().split()))
#     n,d=info[:-1:2],info[1::2]
#     for next,distance in zip(n,d):
#         graph[node]+=[(next,distance)]
# for node in range(1,v+1):
#     visited=[0]*(v+1)
#     bfs(node)
#     result=max(result,max(visited)-1)
# print(result)

# import sys
# input=sys.stdin.readline

# def dfs(now,d):
#     global result
#     result=max(result,d)
#     for next,distance in graph[now]:
#         if not visited[next]:
#             visited[next]=1
#             dfs(next,d+distance)
#             visited[next]=0

# v=int(input())
# graph=[[] for _ in range(v+1)]
# visited=[0]*(v+1)
# for _ in range(v):
#     node,*info=list(map(int,input().split()))
#     n,d=info[:-1:2],info[1::2]
#     for next,distance in zip(n,d):
#         graph[node]+=[(next,distance)]
# result=0
# for node in range(1,v+1):
#     visited[node]=1
#     dfs(node,0)
#     visited[node]=0
# print(result)

# import sys
# input=sys.stdin.readline

# def dfs(now,d):
#     global result
#     result=max(result,d)
#     visited[now]=1
#     for i in range(1,v+1):
#         if not visited[i] and graph[now][i]:
#             visited[i]=1
#             dfs(i,d+graph[now][i])
#             visited[i]=0

# v=int(input())
# graph=[[0]*(v+1) for _ in range(v+1)]
# visited=[0]*(v+1)
# for _ in range(v):
#     node,*info=list(map(int,input().split()))
#     n,d=info[:-1:2],info[1::2]
#     for next,distance in zip(n,d):
#         graph[node][next]=distance
# result=0
# for node in range(1,v+1):
#     dfs(node,0)
# print(result)