import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(a, b, c, prev1, prev2, path):
    if (a, b, c) == (0, 0, 0):
        print(path)
        exit()

    if (a, b, c, prev1, prev2) in visited:
        return

    visited.add((a, b, c, prev1, prev2))
    if a > 0:
        dfs(a - 1, b, c, 'A', prev1, path + 'A')

    if b > 0 and prev1 != 'B':
        dfs(a, b - 1, c, 'B', prev1, path + 'B')

    if c > 0 and 'C' not in [prev1, prev2]:
        dfs(a, b, c - 1, 'C', prev1, path + 'C')


s = input().rstrip()
n = len(s)
d = {'A': 0, 'B': 0, 'C': 0}
for a in s:
    d[a] += 1

visited = set()
dfs(d['A'], d['B'], d['C'], '', '', '')
print(-1)
