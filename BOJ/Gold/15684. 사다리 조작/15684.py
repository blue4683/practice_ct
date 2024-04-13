import sys
input = sys.stdin.readline


def check():
    for x in range(n):
        now = x
        for y in range(h):
            if ladders[y][now]:
                now += 1

            elif now > 0 and ladders[y][now - 1]:
                now -= 1

        if now != x:
            return 0

    return 1


def start_game(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return

    elif cnt == 3 or result <= cnt:
        return

    for i in range(x, h):
        if i == x:
            now = y

        else:
            now = 0

        for j in range(now, n - 1):
            if not ladders[i][j] and not ladders[i][j + 1]:
                if j > 0 and ladders[i][j - 1]:
                    continue

                ladders[i][j] = 1
                start_game(cnt + 1, i, j + 2)
                ladders[i][j] = 0


n, m, h = map(int, input().split())
ladders = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = 1

result = 4
start_game(0, 0, 0)
print(result if result < 4 else -1)
