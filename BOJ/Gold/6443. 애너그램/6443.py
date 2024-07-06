from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(depth, arr):
    if depth == len(str_arr):
        print(''.join(arr))

    for string in visited:
        if visited[string]:
            visited[string] -= 1
            arr.append(string)
            dfs(depth + 1, arr)
            arr.pop()
            visited[string] += 1


n = int(input())
arr = [sorted(input().rstrip()) for _ in range(n)]

for str_arr in arr:
    visited = defaultdict(int)
    for s in str_arr:
        visited[s] += 1

    dfs(0, [])
