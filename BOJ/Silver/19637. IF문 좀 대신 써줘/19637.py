import sys
input = sys.stdin.readline


def bisect(ovr):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if ovr <= limit[mid]:
            r = mid - 1

        else:
            l = mid + 1

    return name[r + 1]


n, m = map(int, input().split())
name = []
limit = []

for _ in range(n):
    a, b = input().rstrip().split()
    name.append(a)
    limit.append(int(b))

for _ in range(m):
    ovr = int(input())
    print(bisect(ovr))
