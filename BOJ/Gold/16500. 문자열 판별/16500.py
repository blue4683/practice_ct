import sys
input = sys.stdin.readline


def dfs(pos):
    if pos == len(string):
        return 1

    if dp[pos] != -1:
        return dp[pos]

    dp[pos] = 0
    for word in words:
        m = len(word)
        if len(string) - pos < m:
            continue

        if string[pos:pos + m] == word:
            dp[pos] |= dfs(pos + m)

    return dp[pos]


string = input().rstrip()
n = int(input())
words = [input().rstrip() for _ in range(n)]

dp = [-1] * len(string)
print(dfs(0))
