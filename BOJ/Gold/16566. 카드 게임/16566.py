import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = sorted(map(int, input().split()))
cards = tuple(map(int, input().split()))
used = [0] * m

for card in cards:
    l, r = 0, m - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > card:
            r = mid

        else:
            l = mid + 1

    for i in range(r, m):
        if not used[i]:
            used[i] = 1
            print(arr[i])
            break
