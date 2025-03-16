from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([s])
    while q:
        x = q.popleft()
        for dx in [u, -d]:
            xx = x + dx
            if xx < 1 or xx > f or arr[xx]:
                continue

            if xx == g:
                return arr[x]
            
            arr[xx] = arr[x] + 1
            q.append(xx)

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
if s == g:
    print(0)

else:
    arr = [0] * (f + 1)
    arr[s] = 1
    print(bfs())
