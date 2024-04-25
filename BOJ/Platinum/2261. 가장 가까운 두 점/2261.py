import sys
input = sys.stdin.readline


def compute(start, end):
    dist = 10 ** 10
    for i in range(start, end - 1):
        x1, y1 = points[i]
        for j in range(i + 1, end):
            x2, y2 = points[j]
            dist = min(dist, (x1 - x2) ** 2 + (y1 - y2) ** 2)

    return dist


def find(start, end):
    size = end - start
    if size < 3:
        return compute(start, end)

    mid = (start + end) // 2
    left, right = find(start, mid), find(mid + 1, end)
    dist = min(left, right)

    check_point = []
    divide_x = points[mid][0]
    for i in range(start, end):
        if (points[i][0] - divide_x) ** 2 <= dist:
            check_point.append(points[i])

    check_point.sort(key=lambda x: x[1])

    for i in range(len(check_point)):
        now_x, now_y = check_point[i]
        for j in range(i + 1, len(check_point)):
            next_x, next_y = check_point[j]
            if (next_y - now_y) ** 2 >= dist:
                break

            dist = min(dist, (now_x - next_x) ** 2 + (now_y - next_y) ** 2)

    return dist


n = int(input())
points = sorted([list(map(int, input().split())) for _ in range(n)])
print(find(0, n))
