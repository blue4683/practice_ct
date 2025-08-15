import sys
input = sys.stdin.readline

while 1:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [arr[0]]
        for i in range(1, n):
            if dp[-1] < arr[i]:
                dp.append(arr[i])

            else:
                l, r = 0, len(dp) - 1
                while l < r:
                    m = (l + r) // 2
                    if dp[m] < arr[i]:
                        l = m + 1

                    else:
                        r = m

                dp[r] = arr[i]

        print(len(dp))

    except:
        break
