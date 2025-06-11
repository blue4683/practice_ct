from itertools import combinations
import sys
input = sys.stdin.readline
MOD = 1000000007


def solution(depth, a, b, c):
    if not depth:
        return 1 if (a, b, c) == (0, 0, 0) else 0

    if a < 0 or b < 0 or c < 0 or (a + b + c) < depth:
        return 0

    if dp[depth][a][b][c] != -1:
        return dp[depth][a][b][c]

    result = 0
    for dd in d:
        aa = a - 1 if 0 in dd else a
        bb = b - 1 if 1 in dd else b
        cc = c - 1 if 2 in dd else c
        result += solution(depth - 1, aa, bb, cc)
        result %= MOD

    dp[depth][a][b][c] = result
    return result


s, *arr = list(map(int, input().split()))

dp = [[[[-1] * (s + 1) for _ in range(s + 1)]
       for _ in range(s + 1)] for _ in range(s + 1)]
d = [dd for i in range(1, 4) for dd in combinations(range(3), i)]
print(solution(s, *arr))
