import sys
input = sys.stdin.readline


def get_stats(team):
    m = len(team)
    stats = 0
    for i in range(m):
        for j in range(i + 1, m):
            stats += arr[team[i]][team[j]] + arr[team[j]][team[i]]

    return stats


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 10 ** 9
for bit in range(1, 1 << (n - 1)):
    start, link = [], []
    for i in range(n):
        if bit & (1 << i):
            link.append(i)

        else:
            start.append(i)

    result = min(result, abs(get_stats(start) - get_stats(link)))

print(result)
