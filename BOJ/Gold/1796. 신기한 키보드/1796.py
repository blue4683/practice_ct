import sys
input = sys.stdin.readline


def get_dist(a, b, c, d):
    if -1 in [c, d]:
        return 0

    return abs(a - c) + abs(c - d) + abs(d - b)


def dfs(alp, pos):
    if alp == 26:
        return 0

    result = dp[pos][alp]
    if result != -1:
        return result

    result = 10 ** 9
    pl, pr = pos_l[alp], pos_r[alp]
    if exist[alp]:
        for i in range(n):
            result = min(result, dfs(alp + 1, i) +
                         min(get_dist(pos, i, pl, pr), get_dist(pos, i, pr, pl)))

    else:
        result = dfs(alp + 1, pos)

    dp[pos][alp] = result
    return dp[pos][alp]


s = input().rstrip()
n = len(s)
dp = [[-1] * 26 for _ in range(n + 1)]
exist = [0] * 26
pos_l, pos_r = [1001] * 26, [-1] * 26
for i in range(n):
    c = s[i]
    alp = ord(c) - ord('a')
    exist[alp] = 1
    pos_l[alp] = min(pos_l[alp], i)
    pos_r[alp] = max(pos_r[alp], i)

print(dfs(0, 0) + n)
