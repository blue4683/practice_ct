from collections import deque
import sys
import math
input = sys.stdin.readline


def bfs():
    q = deque(pwds)
    pivot = int(math.log2(n)) + 1
    while q:
        pwd = q.popleft()
        for i in range(pivot):
            tmp = pwd ^ (1 << i)
            if tmp <= n and safety[tmp] > safety[pwd] + 1:
                safety[tmp] = safety[pwd] + 1
                q.append(tmp)

    return max(safety)


n = int(input())
m = int(input())
pwds = list(map(int, input().split()))
safety = [1e9] * (n + 1)
for pwd in pwds:
    safety[pwd] = 0

print(bfs())
