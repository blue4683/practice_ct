from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
m = len(str(n))

result = 0
visited = set()
visited.add((n, 0))
q = deque([(n, 0)])
while q:
    num, cnt = q.popleft()
    if cnt == k:
        result = max(result, num)
        continue

    lnum = list(str(num))
    for i in range(m - 1):
        for j in range(i + 1, m):
            if not i and lnum[j] == '0':
                continue

            lnum[i], lnum[j] = lnum[j], lnum[i]
            inum = int(''.join(lnum))
            if (inum, cnt + 1) not in visited:
                q.append((inum, cnt + 1))
                visited.add((inum, cnt + 1))

            lnum[i], lnum[j] = lnum[j], lnum[i]

print(result) if result else print(-1)
