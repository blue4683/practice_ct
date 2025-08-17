import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])

    else:
        l, r = 0, len(dp) - 1
        while l < r:
            m = (l + r) // 2
            if arr[i] > dp[m]:
                l = m + 1

            else:
                r = m

        dp[r] = arr[i]

print(len(dp))
