def dfs(depth, result):
    if depth == n:
        print(result)
        return
    
    for i in range(2):
        dfs(depth + 1, result + str(i))

n = int(input())
dfs(0, '')
