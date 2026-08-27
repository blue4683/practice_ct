def solution(n):
    answer = 0
    pos = []
    
    def dfs(depth):
        nonlocal answer
        if depth == n:
            answer += 1
            return
        
        for x in range(n):
            for yy, xx in pos:
                if yy == depth or xx == x or abs(xx - x) == abs(yy - depth):
                    break
                    
            else:
                pos.append((depth, x))
                dfs(depth + 1)
                pos.pop()
    
    dfs(0)
    return answer
