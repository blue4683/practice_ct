def solution(n, info):
    diff, answer = 0, []
    
    def dfs(cnt, score):
        nonlocal answer, diff
        if cnt == n:
            s, t = 0, 0
            for i in range(10):
                if score[i] > info[i]:
                    s += 10 - i
                    
                elif info[i]:
                    t += 10 - i

            if s > t and diff <= s - t:
                answer = score[:]
                diff = s - t
                
            return
        
        for i in range(11):
            if score[i]:
                continue
            
            if cnt + info[i] + 1 <= n:
                score[i] = info[i] + 1
                dfs(cnt + info[i] + 1, score)
            
            else:
                score[i] = n - cnt
                dfs(n, score)
                
            score[i] = 0
    
    dfs(0, [0] * 11)
    return answer if answer else [-1]
