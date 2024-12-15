import sys
input = sys.stdin.readline


def make_num(number, i):
    if number == -1:
        return i

    tmp = [i]
    for num in str(number):
        tmp.append(int(num))

    tmp.sort(reverse=True)
    return int(''.join(map(str, tmp)))


n = int(input())
costs = list(map(int, input().split()))
m = int(input())

dp = [-1] * (m + 1)
for k in range(m + 1):
    for i in range(n):
        if k < costs[i]:
            continue

        dp[k] = max(dp[k], make_num(dp[k - costs[i]], i))

print(dp[m])
