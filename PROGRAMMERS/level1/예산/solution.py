def solution(d, budget):
    answer = 0
    d.sort()
    for cost in d:
        if budget - cost >= 0:
            budget -= cost
            answer += 1
            
        else:
            break
            
    return answer
