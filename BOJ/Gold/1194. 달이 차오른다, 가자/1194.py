from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def escape(start):
    global result
    sy, sx = start
    visited[sy][sx][0] = 1
    q = deque([(sy, sx, 0)])

    while q:
        size = len(q)
        while size:
            y, x, key = q.popleft()
            if maze[y][x] == '1':
                print(result)
                return

            for dy, dx in d:
                yy, xx = y + dy, x + dx
                next_key = key
                if 0 <= yy < n and 0 <= xx < m and maze[yy][xx] != '#':
                    if maze[yy][xx] in ('0', '.', '1'):
                        pass

                    elif (1 << (ord(maze[yy][xx]) - ord('A'))) & 0b111111 != 0:
                        if next_key & (1 << (ord(maze[yy][xx]) - ord('A'))) == 0:
                            continue

                    elif (1 << (ord(maze[yy][xx]) - ord('a'))) & 0b111111 != 0:
                        next_key = next_key | (
                            1 << (ord(maze[yy][xx]) - ord('a')))

                    if visited[yy][xx][next_key]:
                        continue

                    q.append((yy, xx, next_key))
                    visited[yy][xx][next_key] = 1

            size -= 1
        result += 1

    print(-1)
    return


n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
visited = [[[0] * (1 << 6) for _ in range(m)] for _ in range(n)]
start = [[y, x] for y in range(n) for x in range(m) if maze[y][x] == '0'][0]
result = 0
escape(start)
