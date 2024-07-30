import sys
input = sys.stdin.readline

n = int(input())
buildings = [0] + list(map(int, input().split()))
n += 1
result = 0

for x1, y1 in enumerate(buildings):
    if not x1:
        continue

    right = 0
    cur_rslope = None
    for x2 in range(x1 + 1, n):
        y2 = buildings[x2]
        rslope = (y2 - y1) / (x2 - x1)

        if cur_rslope is None or cur_rslope < rslope:
            cur_rslope = rslope
            right += 1

    left = 0
    cur_lslope = None
    for x2 in range(x1 - 1, 0, -1):
        y2 = buildings[x2]
        lslope = (y2 - y1) / (x2 - x1)

        if cur_lslope is None or cur_lslope > lslope:
            cur_lslope = lslope
            left += 1

    result = max(result, left + right)

print(result)
