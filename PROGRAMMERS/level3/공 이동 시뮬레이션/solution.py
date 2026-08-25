def solution(n, m, x, y, queries):
    l = len(queries)
    dp_x = [[0, 0] for _ in range(l + 1)]
    dp_y = [[0, 0] for _ in range(l + 1)]
    dp_x[l] = [x, x]
    dp_y[l] = [y, y]
    for i in range(l - 1, -1, -1):
        command, k = queries[i]
        if command < 2:                    # 열(y) 이동 -> 행(x)은 영향 없음
            dp_x[i] = dp_x[i + 1][:]
            lo, hi = dp_y[i + 1]
            
            if command == 0:                # 열 감소: p' = max(p-k, 0)
                new_lo = 0 if lo == 0 else lo + k
                new_hi = hi + k
                
            else:                            # command == 1, 열 증가: p' = min(p+k, m-1)
                new_hi = (m - 1) if hi == m - 1 else hi - k
                new_lo = lo - k
                
            dp_y[i] = [max(0, new_lo), min(m - 1, new_hi)]
        else:                                # 행(x) 이동 -> 열(y)은 영향 없음
            dp_y[i] = dp_y[i + 1][:]
            lo, hi = dp_x[i + 1]
            if command == 2:                 # 행 감소: p' = max(p-k, 0)
                new_lo = 0 if lo == 0 else lo + k
                new_hi = hi + k
                
            else:                            # command == 3, 행 증가: p' = min(p+k, n-1)
                new_hi = (n - 1) if hi == n - 1 else hi - k
                new_lo = lo - k
                
            dp_x[i] = [max(0, new_lo), min(n - 1, new_hi)]
        
        if dp_x[i][0] > dp_x[i][1] or dp_y[i][0] > dp_y[i][1]:
            return 0
    cnt_x = max(0, dp_x[0][1] - dp_x[0][0] + 1)
    cnt_y = max(0, dp_y[0][1] - dp_y[0][0] + 1)
    
    return cnt_x * cnt_y
