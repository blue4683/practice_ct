from collections import defaultdict, deque


def out_of_range(y, x):
    return y < 0 or y >= n or x < 0 or x >= m


def bfs():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(sy, sx, 0)])
    visited = defaultdict(int)
    visited[(sy, sx, 0)] = 1
    while q:
        y, x, bit = q.popleft()
        if bit == full:
            return visited[(y, x, bit)] - 1
        
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[(yy, xx, bit)] or arr[yy][xx] == '#':
                continue
            
            if isinstance(arr[yy][xx], int) and not bit & (1 << arr[yy][xx]):
                visited[(yy, xx, bit | (1 << arr[yy][xx]))] = visited[(y, x, bit)] + 1
                q.append((yy, xx, bit | (1 << arr[yy][xx])))
        
            else:
                visited[(yy, xx, bit)] = visited[(y, x, bit)] + 1
                q.append((yy, xx, bit))
                
    return -1
            

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
sy, sx = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'S'][0]
lights = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'X']
num = 0
for y, x in lights:
    arr[y][x] = num
    num += 1
    
full = 0
for i in range(num):
    full |= (1 << i)

print(bfs())
