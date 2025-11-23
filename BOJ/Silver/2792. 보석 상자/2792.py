import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

l, r = 1, 10 ** 9
while l <= r:
    mid = (l + r) // 2
    if sum(map(lambda x: (x // mid) + int((x % mid) != 0), arr)) > n:
        l = mid + 1

    else:
        r = mid - 1

print(l)
