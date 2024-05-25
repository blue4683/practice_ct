import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def check(string):
    a, b = 0, 0
    n = len(string)
    for i in range(n):
        s = string[i]
        if s in ['a', 'e', 'i', 'o', 'u']:
            a += 1

        else:
            b += 1

    if a >= 1 and b >= 2:
        return 1

    return 0


def dfs(depth, index, string):
    if depth == l:
        if check(string):
            print(string)

        return

    for i in range(index + 1, c):
        dfs(depth + 1, i, string + arr[i])


l, c = map(int, input().split())
arr = input().rstrip().split()
arr.sort()
for i in range(c):
    dfs(1, i, arr[i])
