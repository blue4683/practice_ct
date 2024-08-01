import sys
input = sys.stdin.readline


n, m, l, k = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(k)]

result = 0
for x1, _ in pos:
    for _, y1 in pos:
        cnt = 0
        for x2, y2 in pos:
            if x1 <= x2 <= x1 + l and y1 <= y2 <= y1 + l:
                cnt += 1

            result = max(result, cnt)

print(k - result)
