import sys
input = sys.stdin.readline


def dfs(seq):
    if len(seq) == n:
        print(*seq)
        return

    for i in range(1, n + 1):
        if used[i]:
            continue

        used[i] = 1
        dfs(seq + [i])
        used[i] = 0


n = int(input())
used = [0] * (n + 1)
dfs([])
