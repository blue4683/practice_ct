from collections import defaultdict, deque
import sys
input = sys.stdin.readline
dx = [60, 10, -10, 1, -1]


def bfs():
    q = deque([(0, 0, 0, 0, 0, 0)])
    visited = set()
    while q:
        x, a, b, c, d, e = q.popleft()
        if 0 <= x <= 60 and x not in visited:
            visited.add(x)
            result[x] = [a, b, c, d, e]
            for i in range(4, -1, -1):
                xx = x + dx[i]
                q.append((xx, a + (i == 0), b + (i == 1), c +
                          (i == 2), d + (i == 3), e + (i == 4)))


result = defaultdict(int)
bfs()
for _ in range(int(input())):
    n = int(input())
    m, k = n // 60, n % 60
    res = result[k][:]
    res[0] += m
    print(*res)
