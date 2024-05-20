from collections import deque, defaultdict
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(sz):
    q = deque([(sz, puzzle)])

    while q:
        z, arr = q.popleft()
        cnt = visited[''.join(arr)]
        if arr == result:
            return cnt

        y, x = z // 3, z % 3

        for dy, dx in d:
            new_arr = arr[:]
            yy = y + dy
            xx = x + dx
            if 0 <= yy < 3 and 0 <= xx < 3:
                zz = yy * 3 + xx
                new_arr[z], new_arr[zz] = new_arr[zz], new_arr[z]
                l = ''.join(new_arr)
                if not visited[l]:
                    visited[l] = cnt + 1
                    q.append((zz, new_arr))

    return -1


puzzle = []
for _ in range(3):
    puzzle += input().rstrip().split()

result = ['0'] * 9
for i in range(9):
    if i == 8:
        continue

    result[i] = str(i + 1)

pos = puzzle.index('0')
visited = defaultdict(int)
print(bfs(pos))
