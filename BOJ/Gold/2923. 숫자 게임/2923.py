import sys
input = sys.stdin.readline

n = int(input())
left, right = [0] * 101, [0] * 101
for k in range(1, n + 1):
    a, b = map(int, input().split())
    left[a] += 1
    right[b] += 1

    ltmp, rtmp = left[:], right[:]
    l, r = 0, 100
    result = 0
    while l <= 100 and r > 0:
        if not ltmp[l]:
            l += 1
            continue

        if not rtmp[r]:
            r -= 1
            continue

        result = max(result, l + r)
        if ltmp[l] > rtmp[r]:
            ltmp[l] -= rtmp[r]
            r -= 1

        elif ltmp[l] < rtmp[r]:
            rtmp[r] -= ltmp[l]
            l += 1

        else:
            l += 1
            r -= 1

    print(result)
