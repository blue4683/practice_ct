from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
flowers = []
for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    if m2 < 3:
        continue

    flowers.append((m1 * 100 + d1, m2 * 100 + d2))

flowers.sort()
q = deque(flowers)

end = 301
result = 0
while q:
    if end >= 1201 or q[0][0] > end:
        break

    tmp = -1
    while q:
        if q[0][0] <= end:
            if tmp <= q[0][1]:
                tmp = q[0][1]

            q.popleft()

        else:
            break

    end = tmp
    result += 1

print(result) if end >= 1201 else print(0)
