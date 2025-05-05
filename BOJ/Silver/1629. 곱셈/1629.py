import sys
input = sys.stdin.readline


def dfs(cnt):
    if cnt == 0:
        return 1

    x = dfs(cnt // 2)
    if cnt % 2:
        return (x * x * a) % c

    else:
        return (x * x) % c


a, b, c = map(int, input().split())
print(dfs(b))
