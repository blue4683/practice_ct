import sys
input = sys.stdin.readline


x, y, c = map(float, input().split())
l, r = 0, min(x, y)
while abs(l - r) >= 10 ** -6:
    mid = (l + r) / 2.0
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5
    h = (h1 * h2) / (h1 + h2)

    if h >= c:
        l = mid

    else:
        r = mid

print(f'{l:.3f}')
