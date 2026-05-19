def solution(info, n, m):
    INF = 10 ** 9
    answer = INF
    k = len(info)
    visited = set()
    def dfs(depth, a, b):
        nonlocal answer
        if a >= answer or (depth, a, b) in visited:
            return
        
        visited.add((depth, a, b))
        if depth == k:
            answer = min(answer, a)
            return
        
        if info[depth][1] + b < m:
            dfs(depth + 1, a, b + info[depth][1])
        
        if info[depth][0] + a < n:
            dfs(depth + 1, a + info[depth][0], b)
    
    dfs(0, 0, 0)
    return answer if answer != INF else -1
