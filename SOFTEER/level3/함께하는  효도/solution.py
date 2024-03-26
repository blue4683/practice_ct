import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(depth, i, y, x, path):
    if depth == 3:
        roots[i].append(path)
        return

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx]:
            visited[yy][xx] = 1
            dfs(depth + 1, i, yy, xx, path + [(yy, xx)])
            visited[yy][xx] = 0

    return 0


n, m = map(int, input().split())
berries = [list(map(int, input().split())) for _ in range(n)]
friends = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

visited = [[0] * n for _ in range(n)]
for y, x in friends:
    visited[y][x] = 1

roots = [[] for _ in range(m)]
for i in range(m):
    y, x = friends[i]
    dfs(0, i, y, x, [(y, x)])

possible = roots[0]
for i in range(1, m):
    tmp = []
    for root1 in possible:
        for root2 in roots[i]:
            for pos1 in root1:
                if pos1 in root2:
                    break
            else:
                tmp.append(root1 + root2)

    possible = tmp

result = 0
for root in possible:
    harvest = 0
    for y, x in root:
        harvest += berries[y][x]

    result = max(result, harvest)

print(result)
