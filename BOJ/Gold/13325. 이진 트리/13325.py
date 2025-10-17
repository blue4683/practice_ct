import sys
input = sys.stdin.readline


def dfs(node):
    global result
    l, r = node * 2, node * 2 + 1
    if l > n:
        return 0

    left_sum = dfs(l) + graph[l]
    right_sum = dfs(r) + graph[r]

    diff = abs(left_sum - right_sum)
    result += diff

    return max(left_sum, right_sum)


k = int(input())
n = 2 ** (k + 1) - 1
graph = [0, 0] + list(map(int, input().split()))

result = sum(graph)
dfs(1)
print(result)
