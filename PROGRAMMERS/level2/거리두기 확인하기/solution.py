def solution(places):
    answer = []
    
    def find(place):
        global visited, n, m
        n, m = len(place), len(place[0])
        visited = [[0] * m for _ in range(n)]
        for y in range(n):
            for x in range(m):
                if place[y][x] == 'P' and not visited[y][x]:
                    if not check(y, x):
                        return 0
                        
        return 1    
    
    def check(sy, sx):
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = [(sy, sx, 0)]
        visited[sy][sx] = 1
        while q:
            y, x, dist = q.pop()
            if dist > 1:
                continue
            
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if yy < 0 or yy >= n or xx < 0 or xx >= m or place[yy][xx] == 'X' or visited[yy][xx]:
                    continue
                    
                if place[yy][xx] == 'P':
                    return 0
                
                visited[yy][xx] = 1
                q.append((yy, xx, dist + 1))
                
        return 1
    
    for place in places:
        answer.append(find(place))
                
    return answer
