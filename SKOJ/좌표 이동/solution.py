INF = float('inf')
n, x, t = map(int, input().split())
methods = [[tuple(map(int, input().split())) for _ in range(int(input()))] for _ in range(n)]

cur = {x: 0}
for i in range(n):
    nxt = {}
    for pos, cost in cur.items():
        for d, c in methods[i]:
            npos = pos + d
            ncost = cost + c
            if npos not in nxt or ncost < nxt[npos]:
                nxt[npos] = ncost
    cur = nxt
    if not cur:
        break

print(cur.get(t, -1))
