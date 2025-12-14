import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
target = [list(map(int, list(input().rstrip()))) for _ in range(n)]

result = 0
for y in range(n - 2):
    for x in range(m - 2):
        if arr[y][x] != target[y][x]:
            result += 1
            for dy in range(3):
                for dx in range(3):
                    arr[y + dy][x + dx] ^= 1

print(-1) if arr != target else print(result)
