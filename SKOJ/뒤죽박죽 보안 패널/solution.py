from collections import deque
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= 3 or x < 0 or x >= 3:
        return 1
    
    return 0


def bfs(start):
    q = deque([start])
    dist = {start: 0}
    while q:
        now = q.popleft()
        if now == init:
            return dist[now]
        
        cur = now.index('0')
        y, x = cur // 3, cur % 3
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue
            
            nz = yy * 3 + xx
            nxt = list(now)
            nxt[cur], nxt[nz] = nxt[nz], nxt[cur]
            nxt = ''.join(nxt)
            if nxt in dist:
                continue
            
            dist[nxt] = dist[now] + 1
            q.append(nxt)
            
    return -1
            
    
arr = ''
for _ in range(3):
    arr += ''.join(input().split())
    
init = '123456780'
print(bfs(arr))
