import sys
input = sys.stdin.readline


def dfs(depth, num, nums):
    global result
    if depth >= result[0]:
        return

    if num == 1:
        if result[0] > depth:
            result = (depth, nums[:])

        return

    if not num % 3:
        dfs(depth + 1, num // 3, nums + [num // 3])

    if not num % 2:
        dfs(depth + 1, num // 2, nums + [num // 2])

    dfs(depth + 1, num - 1, nums + [num - 1])


n = int(input())
result = (10 ** 6, [])
dfs(0, n, [n])

print(result[0])
print(*result[1])
