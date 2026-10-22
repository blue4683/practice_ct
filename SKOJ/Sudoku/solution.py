def dfs(depth):
    if depth == n:
        for l in arr:
            print(*l)
            
        return 1

    y, x = pos[depth]
    b = 3 * (y // 3) + x // 3
    for num in range(1, 10):
        if num in row[y] or num in col[x] or num in box[b]:
            continue
        
        arr[y][x] = num
        row[y].add(num)
        col[x].add(num)
        box[b].add(num)
        if dfs(depth + 1):
            return 1
        
        arr[y][x] = 0
        row[y].discard(num)
        col[x].discard(num)
        box[b].discard(num)
    
    return 0


arr = [list(map(int, input().split())) for _ in range(9)]
pos = []
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
box = [set() for _ in range(9)]
for y in range(9):
    for x in range(9):
        if arr[y][x]:
            row[y].add(arr[y][x])
            col[x].add(arr[y][x])
            box[3 * (y // 3) + x // 3].add(arr[y][x])
            
        else:
            pos.append((y, x))

n = len(pos)
dfs(0)
