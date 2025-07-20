import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
diff = [[0] * n for _ in range(n)]
for s in range(n):
    a, b = 10 ** 9, 0
    for e in range(s, n):
        a = arr[e] if a > arr[e] else a
        b = arr[e] if b < arr[e] else b
        diff[s][e] = b - a

dp = [0] * n
for e in range(n):
    for s in range(e):
        dp[e] = max(dp[e], dp[s] + diff[s + 1][e])

    dp[e] = max(dp[e], dp[e - 1], diff[0][e])

print(dp[n - 1])
