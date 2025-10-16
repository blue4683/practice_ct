from collections import deque
import sys
input = sys.stdin.readline


def out_of_range(x):
    if x < 0 or x >= 9:
        return 1

    return 0


def bfs():
    d = [-3, 3, 1, -1, 0]
    bits = []
    for bit in range(9):
        x = 0
        for dx in d:
            if out_of_range(bit + dx) or (dx in {1, -1} and (bit // 3) != ((bit + dx) // 3)):
                continue

            x ^= (1 << (bit + dx))

        bits.append(x)

    visited = set()
    q = deque([(0, 0)])
    while q:
        x, cnt = q.popleft()
        if x == target:
            return cnt

        for bit in bits:
            xx = x ^ bit
            if xx in visited:
                continue

            visited.add(xx)
            q.append((xx, cnt + 1))

    return -1


for _ in range(int(input())):
    arr = [list(map(lambda x: 1 if x == '*' else 0, list(input().rstrip())))
           for _ in range(3)]
    target = 0
    for y in range(3):
        for x in range(3):
            if arr[y][x]:
                target |= 1 << (y * 3 + x)

    print(bfs())
