def solution(arr):
    if sum(map(sum, arr)) in {len(arr) * len(arr), 0}:
        return [int(0 == arr[0][0]), int(1 == arr[0][0])]
    
    def quad_zip(arr, sy, sx, ey, ex):
        n = ey - sy
        if n == 1:
            return (int(0 == arr[sy][sx]), int(1 == arr[sy][sx]))
        
        total = [0, 0]
        m = n // 2
        sq = [(sy, sx), (sy + m, sx), (sy, sx + m), (sy + m, sx + m)]
        for yy, xx in sq:
            cnt = [0, 0]
            for y in range(yy, yy + m):
                for x in range(xx, xx + m):
                    cnt[arr[y][x]] += 1
                    
            if 0 not in cnt:
                cnt = quad_zip(arr, yy, xx, yy + m, xx + m)   
                total[0] += cnt[0]
                total[1] += cnt[1]
                
            else:
                total[cnt.index(0) ^ 1] += 1
    
        return total
        
    answer = quad_zip(arr, 0, 0, len(arr), len(arr))
    return answer
