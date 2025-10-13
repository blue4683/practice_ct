from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (0, -1), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
directions = [(0, 4, 4), (0, 5, 5), (1, 6, 6), (1, 4, 4),
              (2, 7, 7), (2, 6, 6), (3, 7, 7), (3, 5, 5)]


def out_of_range(r, c):
    if r < 0 or r >= 10 or c < 0 or c >= 9:
        return 1

    return 0


def bfs():
    q = deque([(sr, sc)])
    visited = [[0] * 9 for _ in range(10)]
    visited[sr][sc] = 1
    while q:
        r, c = q.popleft()
        if (r, c) == (er, ec):
            return visited[r][c] - 1

        for direction in directions:
            rr, cc = r, c
            for i in range(3):
                dr, dc = d[direction[i]]
                rr, cc = rr + dr, cc + dc
                if out_of_range(rr, cc) or (i != 2 and (rr, cc) == (er, ec)):
                    break

            else:
                if visited[rr][cc]:
                    continue

                visited[rr][cc] = visited[r][c] + 1
                q.append((rr, cc))

    return -1


sr, sc = map(int, input().split())
er, ec = map(int, input().split())
print(bfs())
