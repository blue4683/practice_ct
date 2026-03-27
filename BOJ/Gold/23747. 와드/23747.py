import sys
input = sys.stdin.readline
drt = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def bfs(sr, sc):
    q = [(sr, sc)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] != arr[sr][sc] or visited[yy][xx] == '.':
                continue

            visited[yy][xx] = '.'
            q.append((yy, xx))


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
nr, nc = map(lambda x: int(x) - 1, input().split())

visited = [['#' for _ in range(c)] for _ in range(r)]
for direction in input().rstrip():
    if direction == 'W':
        visited[nr][nc] = '.'
        bfs(nr, nc)

    else:
        dr, dc = d[drt[direction]]
        nr, nc = nr + dr, nc + dc

visited[nr][nc] = '.'
for dr, dc in d:
    rr, cc = nr + dr, nc + dc
    if out_of_range(rr, cc):
        continue

    visited[rr][cc] = '.'


for l in visited:
    print(''.join(l))
