def dfs(depth):
    global result
    if depth == n:
        result += 1
        return
    
    for x in range(n):
        for yy, xx in pos:
            if yy == depth or xx == x or abs(xx - x) == abs(yy - depth):
                break
                
        else:
            pos.append((depth, x))
            dfs(depth + 1)
            pos.pop()


n = int(input())
pos = []
result = 0

dfs(0)
print(result)
