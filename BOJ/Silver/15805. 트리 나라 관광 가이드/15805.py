import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
max_node = len(set(arr))
parent = -1
graph = [-2] * max_node
for node in arr:
    if graph[node] == -2:
        graph[node] = parent

    parent = node

print(max_node)
print(*graph)
