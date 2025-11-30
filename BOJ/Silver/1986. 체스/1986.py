import sys
input = sys.stdin.readline


def out_of_range(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return 1

    return 0


n, m = map(int, input().split())
arr = [[1] * m for _ in range(n)]
queens = list(map(int, input().split()))
knights = list(map(int, input().split()))
pawns = list(map(int, input().split()))
pieces = set()
for i in range(pawns[0]):
    r, c = pawns[1 + i * 2] - 1, pawns[2 + i * 2] - 1
    arr[r][c] = 0
    pieces.add((r, c))

d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(knights[0]):
    r, c = knights[1 + i * 2] - 1, knights[2 + i * 2] - 1
    arr[r][c] = 0
    pieces.add((r, c))
    for dr, dc in d:
        if not out_of_range(r + 2 * dr, c + dc):
            arr[r + 2 * dr][c + dc] = 0

        if not out_of_range(r + dr, c + 2 * dc):
            arr[r + dr][c + 2 * dc] = 0

for i in range(queens[0]):
    r, c = queens[1 + i * 2] - 1, queens[2 + i * 2] - 1
    arr[r][c] = 0
    pieces.add((r, c))

d += [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(queens[0]):
    r, c = queens[1 + i * 2] - 1, queens[2 + i * 2] - 1
    q = d[:]
    for k in range(1, max(n, m)):
        new_q = []
        for dr, dc in q:
            rr, cc = r + dr * k, c + dc * k
            if out_of_range(rr, cc) or (rr, cc) in pieces:
                continue

            arr[rr][cc] = 0
            new_q.append((dr, dc))

        if not new_q:
            break

        q = new_q[:]

print(sum(map(sum, arr)))
