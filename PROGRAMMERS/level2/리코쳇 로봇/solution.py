from collections import deque


def solution(board):
    answer = 0
    INF = 10 ** 9
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = len(board), len(board[0])

    def out_of_range(y, x):
        if y < 0 or y >= n or x < 0 or x >= m:
            return 1

        return 0

    def bfs(sy, sx):
        q = deque([(sy, sx)])
        visited = [[INF] * m for _ in range(n)]
        visited[sy][sx] = 0
        while q:
            y, x = q.popleft()
            if board[y][x] == 'G':
                return visited[y][x]

            for dy, dx in d:
                yy, xx = y, x
                while not out_of_range(yy + dy, xx + dx) and board[yy + dy][xx + dx] != 'D':
                    yy, xx = yy + dy, xx + dx

                if visited[yy][xx] > visited[y][x] + 1:
                    visited[yy][xx] = visited[y][x] + 1
                    q.append((yy, xx))

        return -1

    sy, sx = [(y, x) for y in range(n)
              for x in range(m) if board[y][x] == 'R'][0]
    answer = bfs(sy, sx)
    return answer
