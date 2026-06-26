def solution(want, number, discount):
    check = {w: n for w, n in zip(want, number)}
    d = {w: 0 for w in want}
    for i in range(10):
        if discount[i] not in d:
            d[discount[i]] = 0
            
        d[discount[i]] += 1
    
    def check_want():
        for w in check:
            if w not in d or d[w] < check[w]:
                return 0
            
        return 1
        
    answer = check_want()
    n = len(discount)
    for i in range(10, n):
        d[discount[i - 10]] -= 1
        if discount[i] not in d:
            d[discount[i]] = 0
            
        d[discount[i]] += 1
        if check_want():
            answer += 1
        
    return answer
