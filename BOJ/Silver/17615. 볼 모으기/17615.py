import sys
input = sys.stdin.readline

n = int(input())
balls = input().rstrip()
red = balls.count('R')
blue = n - red
result = min(red, blue)

cnt = 0
for i in range(n):
    if balls[0] != balls[i]:
        break

    cnt += 1

result = min(result, red - cnt) if balls[0] == 'R' else min(result, blue - cnt)

cnt = 0
for i in range(n - 1, -1, -1):
    if balls[n - 1] != balls[i]:
        break

    cnt += 1

result = min(result, red - cnt) if balls[n -
                                         1] == 'R' else min(result, blue - cnt)
print(result)
