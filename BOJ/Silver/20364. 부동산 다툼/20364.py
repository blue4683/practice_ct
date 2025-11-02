import sys
input = sys.stdin.readline


def check(x):
    xx = x
    node = 0
    while x:
        if graph[x]:
            node = x

        x //= 2

    if not node:
        graph[xx] = 1

    return node


n, q = map(int, input().split())
graph = [0] * (n + 1)
for _ in range(q):
    x = int(input())
    print(check(x))
