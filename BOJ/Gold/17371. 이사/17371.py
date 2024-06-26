import sys
input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


n = int(input())
convs = [tuple(map(int, input().split())) for _ in range(n)]
min_dist = 2 * 10 ** 8
result = convs[0]

for i in range(n):
    hx, hy = convs[i]
    max_dist = 0
    for j in range(n):
        cx, cy = convs[j]
        dist = get_distance(hx, hy, cx, cy)
        max_dist = max(max_dist, dist)

    if min_dist > max_dist:
        min_dist = max_dist
        result = (hx, hy)

print(*result)
