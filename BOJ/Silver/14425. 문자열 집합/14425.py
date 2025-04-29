import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set([input().rstrip() for _ in range(n)])
result = 0

for word in [input().rstrip() for _ in range(m)]:
    if word in s:
        result += 1

print(result)
