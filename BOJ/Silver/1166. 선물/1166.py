import sys
input = sys.stdin.readline

n, l, w, h = map(int, input().split())

s, e = 0, max(l, w, h)
for _ in range(100):
    mid = (s + e) / 2
    if (l // mid) * (w // mid) * (h // mid) >= n:
        s = mid

    else:
        e = mid

print('%.10f' % e)
