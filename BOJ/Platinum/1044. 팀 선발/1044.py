import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
score = [[], []]

for i in range(2):
    score[i] = list(map(int, input().split()))
    if i == 1:
        score[i] = [-x for x in score[i]]

pivot = n // 2

v = [[[] for _ in range(2)] for _ in range(40)]
for k in range(2):
    for bit in range(1 << pivot):
        diff = 0
        cntOn = 0
        for i in range(pivot):
            isOn = (bit & (1 << (pivot - i - 1))) != 0
            diff += score[isOn][i + (pivot if k else 0)]
            if isOn:
                cntOn += 1

        v[cntOn][k].append((diff, bit))

for i in range(pivot + 1):
    new = []
    last = float('inf')

    for diff, bit in sorted(v[i][1]):
        if diff == last:
            continue

        new.append((diff, bit))
        last = diff

    v[i][1] = new

ans = [float('inf'), float('inf')]
for i in range(pivot + 1):
    for diff1, bit1 in v[i][0]:
        reverse = pivot - i
        target = -diff1
        if not v[reverse][1]:
            continue

        idx = bisect_left(v[reverse][1], (target, 0))
        if idx < len(v[reverse][1]):
            diff2, bit2 = v[reverse][1][idx]
            ans = min(ans, [abs(diff1 + diff2), bit1 << pivot | bit2])

        if idx > 0:
            diff2, bit2 = v[reverse][1][idx - 1]
            ans = min(ans, [abs(diff1 + diff2), bit1 << pivot | bit2])

bit = ans[1]
for i in range(n):
    print("12"[(bit & (1 << (n - 1 - i))) != 0], end=' ')
