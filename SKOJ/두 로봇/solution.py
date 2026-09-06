from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def out_of_range(y, x):
    return y < 0 or y >= n or x < 0 or x >= m


def bfs():
    q = deque([(sy_a, sx_a, sy_b, sx_b, 0)])
    visited = set([(sy_a, sx_a, sy_b, sx_b)])
    while q:
        y_a, x_a, y_b, x_b, cnt = q.popleft()
        if (y_a, x_a, y_b, x_b) == (ey_a, ex_a, ey_b, ex_b):
            return cnt
        
        for dy, dx in d:
            if (y_a, x_a) == (ey_a, ex_a):
                yy_a, xx_a = y_a, x_a
                
            else:
                yy_a, xx_a = y_a + dy, x_a + dx
                if out_of_range(yy_a, xx_a) or arr[yy_a][xx_a] == '#':
                    yy_a, xx_a = y_a, x_a

            if (y_b, x_b) == (ey_b, ex_b):
                yy_b, xx_b = y_b, x_b
                
            else:
                yy_b, xx_b = y_b + dy, x_b + dx
                if out_of_range(yy_b, xx_b) or arr[yy_b][xx_b] == '#':
                    yy_b, xx_b = y_b, x_b

            if (yy_a, xx_a) == (y_b, x_b) and (yy_b, xx_b) == (y_a, x_a):
                continue
            
            if (yy_a, xx_a, yy_b, xx_b) not in visited and (yy_a, xx_a) != (yy_b, xx_b):
                visited.add((yy_a, xx_a, yy_b, xx_b))
                q.append((yy_a, xx_a, yy_b, xx_b, cnt + 1))
                
    return -1
    

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
sy_a, sx_a = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'A'][0]
ey_a, ex_a = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'a'][0]
sy_b, sx_b = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'B'][0]
ey_b, ex_b = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'b'][0]

print(bfs())
