import sys
input = sys.stdin.readline


n, h = map(int, input().split())
up, down = [0] * (h + 1), [0] * (h + 1)
for i in range(n):
    if i % 2:
        up[int(input())] += 1

    else:
        down[int(input())] += 1

for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

cnt, result = 10 ** 9, 0
for i in range(1, h + 1):
    obs = up[i] + down[h - i + 1]
    if obs < cnt:
        cnt = obs
        result = 1

    elif obs == cnt:
        result += 1

print(cnt, result)
