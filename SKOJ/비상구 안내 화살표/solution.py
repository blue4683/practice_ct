from collections import deque


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1
    
    return 0


def bfs():
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    arrows = {0: '^', 1: 'v', 2: '<', 3: '>'}
    indexes = {'^': 0, 'v': 1, '<': 2, '>': 3}
    q = deque([])
    for y in range(h):
        for x in range(w):
            if arr[y][x] == 'E':
                q.append((y, x))
                visited[y][x] = 0
                
    while q:
        y, x = q.popleft()
        for i, (dy, dx) in enumerate(d):
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == '#' or visited[yy][xx] < visited[y][x] + 1:
                continue
            
            if visited[yy][xx] == visited[y][x] + 1:
                arr[yy][xx] = arrows[min(i, indexes[arr[yy][xx]])]
                continue
            
            else:
                arr[yy][xx] = arrows[i]
                
            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))
                

h, w = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]
visited = [[10 ** 9] * w for _ in range(h)]
bfs()

for l in arr:
    print(''.join(l))
    