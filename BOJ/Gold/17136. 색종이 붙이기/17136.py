import sys
input = sys.stdin.readline


def check(y, x, size):
    for dy in range(size):
        for dx in range(size):
            if paper[y + dy][x + dx] == 0:
                return 0

    return 1


def fill(y, x, size):
    for dy in range(size):
        for dx in range(size):
            paper[y + dy][x + dx] = 0

    return


def undo(y, x, size):
    for dy in range(size):
        for dx in range(size):
            paper[y + dy][x + dx] = 1

    return


def dfs(y, x, cnt):
    global result
    if y >= 10:
        result = min(result, cnt)
        return

    if x >= 10:
        dfs(y + 1, 0, cnt)
        return

    if paper[y][x]:
        for size in range(1, 6):
            if used[size] == 5:
                continue

            if y + size > 10 or x + size > 10:
                continue

            if check(y, x, size):
                fill(y, x, size)

                used[size] += 1
                dfs(y, x + size, cnt + 1)
                used[size] -= 1

                undo(y, x, size)

    else:
        dfs(y, x + 1, cnt)


paper = [list(map(int, input().split())) for _ in range(10)]
used = [0] * 6
result = 1e9
dfs(0, 0, 0)

print(result) if result != 1e9 else print(-1)
