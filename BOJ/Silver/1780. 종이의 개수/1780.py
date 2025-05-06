import sys
input = sys.stdin.readline


def dfs(sy, sx, k):
    nums = {arr[sy][sx]}
    flag = 0
    for y in range(sy, sy + k):
        if flag:
            break

        for x in range(sx, sx + k):
            if arr[y][x] not in nums:
                flag = 1
                break

    if flag:
        kk = k // 3
        for y in range(sy, sy + k, kk):
            for x in range(sx, sx + k, kk):
                dfs(y, x, kk)

    else:
        result[nums.pop()] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3
dfs(0, 0, n)

for i in [-1, 0, 1]:
    print(result[i])
