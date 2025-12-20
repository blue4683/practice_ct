import sys
input = sys.stdin.readline


def dfs(x):
    global result
    if x == 11:
        result = max(result, sum(ability))
        return

    for i in range(11):
        if visited[i] or not arr[i][x]:
            continue

        visited[i] = 1
        ability[x] = arr[i][x]
        dfs(x + 1)
        ability[x] = 0
        visited[i] = 0


for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(11)]
    ability = [0] * 11
    visited = [0] * 11
    result = 0
    dfs(0)

    print(result)
