def solution(grid):
    answer = []
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = len(grid), len(grid[0])
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    
    def find(y, x, direction):
        while 1:
            if visited[y][x][direction] == 2:
                return 0
            
            if visited[y][x][direction] == 1:
                path = set()
                while visited[y][x][direction] == 1:
                    if (y, x, direction) in path:
                        break

                    path.add((y, x, direction))
                    if grid[y][x] == 'S':
                        k = 0

                    elif grid[y][x] == 'L':
                        k = -1

                    else:
                        k = 1

                    direction = (direction + k) % 4
                    dy, dx = d[direction]
                    y, x = (y + dy) % n, (x + dx) % m

                for y, x, direction in path:
                    visited[y][x][direction] = 2

                return len(path)

            visited[y][x][direction] = 1
            if grid[y][x] == 'S':
                k = 0

            elif grid[y][x] == 'L':
                k = -1

            else:
                k = 1

            direction = (direction + k) % 4
            dy, dx = d[direction]
            y = (y + dy) % n
            x = (x + dx) % m
    
    for y in range(n):
        for x in range(m):
            for direction in range(4):
                if visited[y][x][direction] == 2:
                    continue
                    
                cnt = find(y, x, direction)
                if cnt:
                    answer.append(cnt)
    
    answer.sort()
    return answer
