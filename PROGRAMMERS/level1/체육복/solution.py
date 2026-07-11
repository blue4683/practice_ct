def solution(n, lost, reserve):
    answer = n - len(lost)
    lost = set(lost)
    reserve = set(reserve)
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.discard(i)
            reserve.discard(i)
            answer += 1
            
    for i in reserve:
        if i - 1 in lost:
            lost.discard(i - 1)
            answer += 1        
    
        elif i + 1 in lost:
            lost.discard(i + 1)
            answer += 1
            
    return answer
