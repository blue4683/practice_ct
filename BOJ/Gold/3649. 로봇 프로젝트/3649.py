import sys
input = sys.stdin.readline


while 1:
    try:
        x, n = [int(input()) for _ in range(2)]
        x *= 10 ** 7
        arr = sorted([int(input()) for _ in range(n)])
        result = 0
        l, r = 0, n - 1
        while l < r:
            if arr[l] + arr[r] == x:
                result = 1
                break

            elif arr[l] + arr[r] > x:
                r -= 1

            else:
                l += 1

        print('danger') if not result else print('yes', arr[l], arr[r])

    except:
        break
