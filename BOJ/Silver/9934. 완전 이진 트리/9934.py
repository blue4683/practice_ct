from collections import deque
import sys
input = sys.stdin.readline


def dfs(node, depth):
    if node > n:
        return

    dfs(2 * node, depth + 1)
    graph[depth].append(arr.popleft())
    dfs(2 * node + 1, depth + 1)


k = int(input())
n = 2 ** k - 1
arr = deque(map(int, input().split()))
graph = [[] for _ in range(k + 1)]
dfs(1, 0)
for l in graph:
    print(*l)
