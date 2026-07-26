def solution(cap, n, deliveries, pickups):
    answer = 0
    l, r = n - 1, n - 1
    while l >= 0 or r >= 0:
        while not deliveries[l] and l >= 0:
            l -= 1
            
        while not pickups[r] and r >= 0:
            r -= 1
            
        inv = 0
        dist = max(l, r) + 1
        while l >= 0 and inv < cap:
            if inv + deliveries[l] <= cap:
                inv += deliveries[l]
                deliveries[l] = 0
                l -= 1
                
            else:
                tmp = cap - inv
                inv += tmp
                deliveries[l] -= tmp
        
        inv = 0
        while r >= 0 and inv < cap:
            if inv + pickups[r] <= cap:
                inv += pickups[r]
                pickups[r] = 0
                r -= 1
                
            else:
                tmp = cap - inv
                inv += tmp
                pickups[r] -= tmp
        
        answer += dist * 2
        
    return answer
