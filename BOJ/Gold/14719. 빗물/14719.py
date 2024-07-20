import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):
    block = blocks[i]
    lpivot, rpivot = max(blocks[:i]), max(blocks[i + 1:])
    pivot = min(lpivot, rpivot)

    if pivot > block:
        result += pivot - block

print(result)
