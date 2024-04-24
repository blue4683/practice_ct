import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

result = 0
left, right = lines[0]

for x, y in lines[1:]:
    if right >= y:
        continue

    elif x <= right < y:
        right = y

    elif right < x:
        result += right - left
        left = x
        right = y

result += right - left
print(result)
