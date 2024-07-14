from collections import deque
import sys
input = sys.stdin.readline

move = [[0, -1], [-1, 0], [0, 1]]


def copy_arr(arr: list):
    new_arr = []
    for l in arr:
        new_arr.append(l[:])

    return new_arr


def get_case(arr: list, c: set):
    if len(c) == 3:
        archors.append(c)
        return

    for pos in arr:
        if pos in c:
            continue

        get_case(arr, c | {pos})


def attack(pos: list):
    castle = copy_arr(arr)
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for ay in range(n - 1, -1, -1):
        dead_soldiers = []
        for ax in pos:
            q = deque([(ay, ax, 1)])
            while q:
                y, x, dist = q.popleft()
                if castle[y][x]:
                    dead_soldiers.append((y, x))
                    if not visited[y][x]:
                        visited[y][x] = 1
                        cnt += 1

                    break

                if dist < d:
                    for dy, dx in move:
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < n and 0 <= xx < m:
                            q.append((yy, xx, dist + 1))

        for y, x in dead_soldiers:
            castle[y][x] = 0

    return cnt


n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

archors = []
get_case([i for i in range(m)], set())

result = 0
for archor in archors:
    result = max(result, attack(archor))

print(result)
