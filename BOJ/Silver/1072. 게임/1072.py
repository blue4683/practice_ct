import sys
input = sys.stdin.readline


x, y = map(int, input().split())

z = int((y * 100) / x)
l, r = 0, x
while l <= r:
    mid = (l + r) // 2
    if int((((y + mid) * 100) / (x + mid))) > z:
        r = mid - 1

    else:
        l = mid + 1

print(l) if l <= x else print(-1)
