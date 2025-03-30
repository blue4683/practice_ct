import sys
input = sys.stdin.readline


def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    op = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if op > 0:
        return 1

    elif op == 0:
        return 0

    else:
        return -1


def is_crossed(line1, line2):
    p1, p2 = line1
    p3, p4 = line2
    x = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    y = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    return x < 0 and y < 0


pos = list(map(int, input().split()))
a, b, c, d = [pos[i * 2:i * 2 + 2] for i in range(4)]
print(int(is_crossed([a, b], [c, d])))
