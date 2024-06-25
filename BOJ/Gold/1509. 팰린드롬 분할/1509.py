import sys
input = sys.stdin.readline


string = input().rstrip()
n = len(string)
palindrome = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    palindrome[i][i] = 1

for i in range(1, n):
    if string[i - 1] == string[i]:
        palindrome[i - 1][i] = 1

for length in range(3, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        if string[start] == string[end] and palindrome[start + 1][end - 1]:
            palindrome[start][end] = 1

dp = [n] * (n + 1)
dp[n] = 0

for end in range(n):
    for start in range(end + 1):
        if palindrome[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)

print(dp[n - 1])
