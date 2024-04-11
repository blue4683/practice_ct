from collections import deque, defaultdict
import sys
input = sys.stdin.readline


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def copy_arr(arr):
    new_arr = []
    for l in arr:
        new_arr.append(l[:])

    return new_arr


def move(y, x, dy, dx):
    cnt = 0
    yy, xx = y, x
    while board[yy + dy][xx + dx] != '#' and board[yy][xx] != 'O':
        yy, xx = yy + dy, xx + dx
        cnt += 1

    return yy, xx, cnt


def bfs(rsy, rsx, bsy, bsx):
    q = deque([[rsy, rsx, bsy, bsx, 1]])
    visited[(rsy, rsx, bsy, bsx)] = 1

    while q:
        ry, rx, by, bx, cnt = q.popleft()
        if cnt > 10:
            return -1

        for dy, dx in d:
            ryy, rxx, rcnt = move(ry, rx, dy, dx)
            byy, bxx, bcnt = move(by, bx, dy, dx)

            if board[byy][bxx] != 'O':
                if board[ryy][rxx] == 'O':
                    return cnt

                if ryy == byy and rxx == bxx:
                    if rcnt > bcnt:
                        ryy, rxx = ryy - dy, rxx - dx

                    else:
                        byy, bxx = byy - dy, bxx - dx

                pos = (ryy, rxx, byy, bxx)
                if not visited[pos]:
                    visited[pos] = 1
                    q.append([*pos, cnt + 1])

    return -1


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
rsy, rsx = [(y, x) for y in range(n)
            for x in range(m) if board[y][x] == 'R'][0]
bsy, bsx = [(y, x) for y in range(n)
            for x in range(m) if board[y][x] == 'B'][0]
visited = defaultdict(int)

print(bfs(rsy, rsx, bsy, bsx))
