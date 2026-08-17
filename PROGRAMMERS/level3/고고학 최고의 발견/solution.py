from itertools import product
def solution(clockHands):
    answer = 10 ** 9
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(clockHands)
    def out_of_range(y, x):
        if y < 0 or y >= n or x < 0 or x >= n:
            return 1
        
        return 0
    
    def rotate(y, x, arr):
        arr[y][x] = (arr[y][x] + 1) % 4
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue
                
            arr[yy][xx] = (arr[yy][xx] + 1) % 4
        
        return arr
            
    def rotate_all(arr):
        cnt = 0
        for x in range(n):
            for _ in range(bit[x]):
                arr = rotate(0, x, arr)
                cnt += 1
        for y in range(1, n):
            for x in range(n):
                while arr[y - 1][x]:
                    arr = rotate(y, x, arr)
                    cnt += 1
        
        return cnt if not sum(map(sum, arr)) else -1
    
    cases = product(range(4), repeat=n)
    for bit in cases:
        arr = [l[:] for l in clockHands]
        cnt = rotate_all(arr)
        if cnt != -1:
            answer = min(answer, cnt)
                    
    return answer
