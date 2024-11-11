from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m, k = 0, 0
balls = []
for i in range(n):
    c, s = map(int, input().split())
    m, k = max(m, s), max(k, c)
    balls.append((s, c, i))

result = [0] * n
scores = [0] * (k + 1)
sizes = [0] * (m + 1)
size_color = defaultdict(int)
total = 0
balls.sort()
for s, c, i in balls:
    result[i] = total - scores[c] - (sizes[s] * s) + (size_color[(c, s)] * s)
    total += s
    scores[c] += s
    sizes[s] += 1
    size_color[(c, s)] += 1

for score in result:
    print(score)
