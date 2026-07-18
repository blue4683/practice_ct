def solution(weights):
    answer = 0
    weights.sort()
    n = len(weights)
    visited = [0] * (weights[-1] + 1)
    for i in range(n):
        if visited[weights[i]]:
            visited[weights[i]] -= 1
            answer += visited[weights[i]]
            continue
            
        for j in range(i + 1, n):
            if weights[i] == weights[j] or weights[i] * 2 == weights[j] or weights[i] * 3 == weights[j] * 2 or weights[i] * 4 == weights[j] * 3:
                visited[weights[i]] += 1
            
            if weights[i] * 2 < weights[j]:
                break
        
        answer += visited[weights[i]]
                
    return answer
