import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
x, y = sorted([x, y])
if w * 2 > s:
    if w > s:
        if not (y - x) % 2:
            print(y * s)

        else:
            print((y - 1) * s + w)

    else:
        print(x * s + (y - x) * w)


else:
    print((x + y) * w)
