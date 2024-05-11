import sys
input = sys.stdin.readline
MAX = 10 ** 6 + 1

n = int(input())
pos = [list(map(lambda x: int(x) + 500000, input().split())) for _ in range(n)]
dp_x = [0] * (MAX + 1)
dp_y = [0] * (MAX + 1)
result = 0

for i in range(n):
    x, y = pos[i]
    xx, yy = pos[(i + 1) % n]

    if x == xx:
        dp_y[min(y, yy)] += 1
        dp_y[max(y, yy)] -= 1

    else:
        dp_x[min(x, xx)] += 1
        dp_x[max(x, xx)] -= 1

for i in range(1, MAX):
    dp_x[i] += dp_x[i - 1]
    dp_y[i] += dp_y[i - 1]
    result = max(result, max(dp_x[i], dp_y[i]))

print(result)
