import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def inorder(node):
    global last_node
    left, right = graph[node]
    if left != -1:
        inorder(left)

    last_node = node
    if right != -1:
        inorder(right)


def traversal(node):
    global result
    result += 1
    left, right = graph[node]
    if left != -1 and not visited[left]:
        visited[left] = 1
        traversal(left)

    elif right != -1 and not visited[right]:
        visited[right] = 1
        traversal(right)

    elif node == last_node:
        return

    else:
        traversal(parents[node])


n = int(input())
parents = [0] * (n + 1)
graph = {}
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a] = [b, c]
    if b != -1:
        parents[b] = a

    if c != -1:
        parents[c] = a

last_node = 0
inorder(1)

visited = [0] * (n + 1)
visited[1] = 1
result = -1
traversal(1)

print(result)
