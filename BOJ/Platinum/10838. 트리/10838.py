import sys
input = sys.stdin.readline


def solution(order):
    if len(order) == 4:
        paint(*order[1:])

    else:
        r, a, b = order
        if r == 2:
            move(a, b)

        else:
            print(count(a, b))


def query(a, b):
    global cnt
    if a == b:
        return a

    cnt += 1

    for _ in range(1000):
        if a:
            if visited[a] == cnt:
                return a

            visited[a] = cnt
            a = parents[a][0]

        if b:
            if visited[b] == cnt:
                return b

            visited[b] = cnt
            b = parents[b][0]

        if a == b and not a:
            return 0


def paint(a, b, c):
    lca = query(a, b)
    while a != lca:
        parents[a][1] = c
        a = parents[a][0]

    while b != lca:
        parents[b][1] = c
        b = parents[b][0]


def move(a, b):
    parents[a][0] = b


def count(a, b):
    lca = query(a, b)
    colors = set()
    while a != lca:
        colors.add(parents[a][1])
        a = parents[a][0]

    while b != lca:
        colors.add(parents[b][1])
        b = parents[b][0]

    return len(colors)


n, k = map(int, input().split())
parents = [[0, 0] for _ in range(n + 1)]
orders = [list(map(int, input().split())) for _ in range(k)]
visited = [0] * (n + 1)
cnt = 0
for order in orders:
    solution(order)
