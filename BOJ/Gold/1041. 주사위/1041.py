import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    result = sum(dice) - max(dice)

else:

    result = min(dice) * ((n - 2) * (n - 2) * 5 + (n - 2) * 4)
    result += min([dice[x] + dice[y] for y in range(6)
                   for x in range(y + 1, 6) if x + y != 5]) * (4 + (n - 2) * 8)
    result += min([dice[x] + dice[y] + dice[z] for z in range(6) for y in range(z + 1, 6)
                   for x in range(y + 1, 6) if 5 not in [x + y, y + z, x + z]]) * 4

print(result)
