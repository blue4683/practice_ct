def solve(pos, used, big, zero):
    if dp[pos][used][big][zero] != -1:
        return dp[pos][used][big][zero]

    if pos == 19:
        if not big:
            return -2

        cnt = bin(used).count('1')
        if cnt != k:
            return -2

        return 0

    ret = 0

    if zero and n[pos] == 0:
        next_val = solve(pos + 1, used, big, zero)
        if next_val >= 0:
            return next_val

    for i in range(0 if big else n[pos], 10):
        if zero and i == 0:
            continue

        next_val = solve(pos + 1, used | (1 << i),
                         big or (i > n[pos]), zero and (i == 0))
        if next_val >= 0:
            ret = next_val + ten[pos] * i
            return ret

    dp[pos][used][big][zero] = -2
    return dp[pos][used][big][zero]


n, k = map(int, input().split())
n = str(n - 1).zfill(19)
n = list(map(int, n))

dp = [[[[-1] * 2 for _ in range(2)]
       for _ in range(1 << 10)] for _ in range(20)]

ten = [0] * 19
for i in range(18, -1, -1):
    ten[i] = 1 if i == 18 else ten[i + 1] * 10

print(solve(0, 0, 0, 1))
