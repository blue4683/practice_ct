def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        v = 1
        for k in range(int(num ** 0.5), 1, -1):
            if not num % k:
                if num // k <= 10000000:
                    v = max(v, num // k)
                    
                else:
                    v = max(v, k)
                
        answer.append(v) if num >= 2 else answer.append(0)
            
    return answer
