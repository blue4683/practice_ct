import sys
input = sys.stdin.readline


def set_depth(depth, node):
    tree_depth[node] = depth
    if graph[node][1] != -1:
        set_depth(depth + 1, graph[node][1])

    if graph[node][2] != -1:
        set_depth(depth + 1, graph[node][2])


def set_width(node):
    global width
    if graph[node][1] != -1:
        set_width(graph[node][1])

    tree[tree_depth[node]][width] = node
    width += 1

    if graph[node][2] != -1:
        set_width(graph[node][2])


n = int(input())
graph = [[-1, -1, -1] for _ in range(n + 1)]
tree_depth = [0] * (n + 1)

for _ in range(n):
    node, left, right = map(int, input().split())
    graph[node][1] = left
    graph[node][2] = right
    graph[left][0] = node
    graph[right][0] = node

root = -1
for node in range(1, n + 1):
    if graph[node][0] == -1:
        root = node

set_depth(1, root)
max_depth = max(tree_depth) + 1
tree = [[0] * (n + 1) for _ in range(max_depth)]
width = 1
set_width(root)

width, depth = 0, max_depth
for y in range(1, max_depth):
    left, right = n + 1, 0
    for x in range(1, n + 1):
        if tree[y][x]:
            left = min(left, x)
            right = max(right, x)

    if right - left + 1 > width:
        width = right - left + 1
        depth = y

print(depth, width)
