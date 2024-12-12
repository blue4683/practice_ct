import sys
input = sys.stdin.readline
INF = 10 ** 10

n, m = map(int, input().split())
meat = [list(map(int, input().split())) for _ in range(n)]
meat.sort(key=lambda x: (x[1], -x[0]))

result, before, cost, weight = INF, -1, 0, 0
for i in range(n):
    mweight, mcost = meat[i]
    if before == mcost:
        cost += mcost

    else:
        cost = mcost

    before = mcost
    weight += mweight
    if weight >= m:
        result = min(result, cost)

print(result if result != INF else -1)
