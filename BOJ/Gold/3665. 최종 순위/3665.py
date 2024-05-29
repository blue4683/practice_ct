from collections import deque
import sys
input = sys.stdin.readline


def topology_sort(indegree, n):
    result = []
    q = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    if len(result) != n:
        print('IMPOSSIBLE')
        return

    print(*result)
    return


def solution():
    n = int(input())
    last_year = list(map(int, input().split()))

    m = int(input())
    if not m:
        print(*last_year)
        return

    last_rank = [0] * (n + 1)
    for i in range(n):
        last_rank[last_year[i]] = i + 1

    indegree = [0] * (n + 1)
    for i in range(n):
        indegree[last_year[i]] = i

    for _ in range(m):
        a, b = map(int, input().split())
        if last_rank[a] < last_rank[b]:
            a, b = b, a

        indegree[a] -= 1
        indegree[b] += 1

    topology_sort(indegree, n)


for _ in range(int(input())):
    solution()
