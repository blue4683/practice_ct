import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]
for i in range(n):
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

print(len(dp) - 1)
