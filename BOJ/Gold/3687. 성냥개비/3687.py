import sys
input = sys.stdin.readline

matches = {2: ['1'], 3: ['7'], 4: ['4'], 5: [
    '2', '3', '5'], 6: ['0', '6', '9'], 7: ['8']}

for _ in range(int(input())):
    n = int(input())
    max_dp = ['0'] * (n + 1)
    min_dp = ['9' * 50] * (n + 1)

    for i in range(2, n + 1):
        for cnt, ms in matches.items():
            for m in ms:
                if i == cnt:
                    if m == '0':
                        continue

                    if max_dp[i] == '0':
                        max_dp[i] = m

                    else:
                        max_dp[i] = str(max(int(max_dp[i]), int(m)))

                    if min_dp[i] == '9' * 50:
                        min_dp[i] = m

                    else:
                        min_dp[i] = str(min(int(min_dp[i]), int(m)))

                elif i - cnt >= 0:
                    max_dp[i] = str(
                        max(int(max_dp[i]), int(max_dp[i - cnt] + m)))

                    min_dp[i] = str(
                        min(int(min_dp[i]), int(min_dp[i - cnt] + m)))

    print(int(min_dp[n]), int(max_dp[n]))
