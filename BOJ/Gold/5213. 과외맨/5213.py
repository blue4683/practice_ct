from collections import deque
import sys
input = sys.stdin.readline


def out_of_range(a, b):
    if b <= 0 or b >= m + 1:
        return 1
    
    if row[a] == row[b] and a - b in [-1, 1]:
        return 0
    
    if row[a] - row[b] == -1 and a - b in [-(n - 1), -n]:
        return 0
    
    if row[a] - row[b] == 1 and a - b in [n - 1, n]:
        return 0

    return 1


def bfs():
    before = [0] * (m + 1)
    visited = [10 ** 9] * (m + 1)
    visited[1] = 1
    q = deque([1])
    while q:
        num = q.popleft()
        for next_num, i, j in [(num - 1, 0, 1), (num + 1, 1, 0), (num - (n - 1), 1, 0), (num - n, 0, 1), (num + (n - 1), 0, 1), (num + n, 1, 0)]:
            if out_of_range(num, next_num) or visited[next_num] <= visited[num] + 1:
                continue

            if tiles[num][i] != tiles[next_num][j]:
                continue
            
            before[next_num] = num
            visited[next_num] = visited[num] + 1
            q.append(next_num)

    target = 0
    for i in range(n * n - n // 2, 0, -1):
        if visited[i] != 10 ** 9:
            target = i
            break

    route = []
    while target > 1:
        route.append(target)
        target = before[target]
        
    route.append(1)
    return route[::-1]


n = int(input())
m = n * n - n // 2
tiles = [(0, 0)]
for _ in range(m):
    tiles.append(tuple(map(int, input().split())))

row = dict()
idx = 1
for i in range(n):
    for _ in range(n - i % 2):
        row[idx] = i
        idx += 1

result = bfs()
print(len(result))
print(*result)
