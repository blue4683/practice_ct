import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
belt += belt[:k]

result = 0
for start in range(n):
    result = max(result, len(set(belt[start:start + k]) | {c}))

print(result)
