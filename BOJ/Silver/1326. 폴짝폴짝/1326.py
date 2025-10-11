from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([a])
    visited = [0] * n
    visited[a] = 1
    while q:
        x = q.popleft()
        if x == b:
            return visited[x] - 1

        for k in [arr[x], -arr[x]]:
            xx = x
            while 1:
                xx += k
                if xx >= n or xx < 0:
                    break

                if visited[xx]:
                    continue

                visited[xx] = visited[x] + 1
                q.append(xx)

    return -1


n = int(input())
arr = list(map(int, input().split()))
a, b = map(lambda x: int(x) - 1, input().split())
print(bfs())
