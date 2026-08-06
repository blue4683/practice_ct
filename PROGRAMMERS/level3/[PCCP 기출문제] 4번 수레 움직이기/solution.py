def solution(maze):
    answer = 10 ** 9
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, b = (), ()
    er, eb = (), ()
    n, m = len(maze), len(maze[0])
    for y in range(n):
        for x in range(m):
            if maze[y][x] == 1:
                r = (y, x)
                
            elif maze[y][x] == 2:
                b = (y, x)
                
            elif maze[y][x] == 3:
                er = (y, x)
                
            elif maze[y][x] == 4:
                eb = (y, x)
    
    rvisited = [[0] * m for _ in range(n)]
    bvisited = [[0] * m for _ in range(n)]
    rvisited[r[0]][r[1]] = 1
    bvisited[b[0]][b[1]] = 1
    def out_of_range(y, x):
        if y < 0 or y >= n or x < 0 or x >= m:
            return 1
        
        return 0
    
    def dfs(depth, ry, rx, by, bx):
        nonlocal answer
        if depth >= answer:
            return

        if ((ry, rx), (by, bx)) == (er, eb):
            answer = min(answer, depth)
            return
        
        for i in range(4):
            for j in range(4):
                if (ry, rx) == er:
                    ryy, rxx = ry, rx
                
                else:
                    rdy, rdx = d[i]
                    ryy, rxx = ry + rdy, rx + rdx

                if (by, bx) == eb:
                    byy, bxx = by, bx
                
                else:
                    bdy, bdx = d[j]
                    byy, bxx = by + bdy, bx + bdx
                    
                if (out_of_range(ryy, rxx) or out_of_range(byy, bxx)) or ((ryy, rxx) == (by, bx) and (byy, bxx) == (ry, rx)) or (ryy, rxx) == (byy, bxx) or 5 in {maze[ryy][rxx], maze[byy][bxx]} or (rvisited[ryy][rxx] or bvisited[byy][bxx]):
                    continue
                
                if (ryy, rxx) != er:
                    rvisited[ryy][rxx] = 1
                    
                if (byy, bxx) != eb:
                    bvisited[byy][bxx] = 1
                    
                dfs(depth + 1, ryy, rxx, byy, bxx)
                rvisited[ryy][rxx] = 0
                bvisited[byy][bxx] = 0

    dfs(0, *r, *b)
    return answer if answer != 10 ** 9 else 0
