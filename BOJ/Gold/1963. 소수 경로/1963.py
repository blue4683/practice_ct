from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    q = deque([a])
    visited = [0] * 10000
    visited[int(a)] = 1
    while q:
        x = q.popleft()
        if x == b:
            return visited[int(x)] - 1

        for i in range(4):
            for num in range(10):
                if num == int(x[i]):
                    continue

                xx = x[:i] + str(num) + x[i + 1:]
                if visited[int(xx)] or not is_prime[int(xx)] or int(xx) < 1000:
                    continue

                visited[int(xx)] = visited[int(x)] + 1
                q.append(xx)

    return 'Impossible'


is_prime = [1] * 10000
is_prime[0], is_prime[1] = 0, 0
for i in range(2, int(10000 ** 0.5) + 1):
    if not is_prime[i]:
        continue

    for j in range(2 * i, 10000, i):
        is_prime[j] = 0

for _ in range(int(input())):
    a, b = input().split()
    if a == b:
        print(0)

    else:
        print(bfs(a, b))
