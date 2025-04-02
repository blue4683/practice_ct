import sys
input = sys.stdin.readline


def check(num):
    cnt = 0
    for a, c, b in arr:
        check_num = min(num, c)
        if check_num < a:
            continue

        else:
            cnt += ((check_num - a) // b) + 1

    return cnt


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

result = 0
l, r = 1, 2147483647
while l <= r:
    mid = (l + r) // 2
    if check(mid) % 2:
        r = mid - 1
        result = mid

    else:
        l = mid + 1

print(result, check(result) - check(result - 1)) if result else print('NOTHING')
