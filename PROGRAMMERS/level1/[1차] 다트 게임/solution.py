def solution(dartResult):
    answer = 0
    n, i, points = len(dartResult), 0, []
    mul = {'S': 1, 'D': 2, 'T': 3}
    while i < n:
        if dartResult[i].isdigit():
            if dartResult[i + 1].isdigit():
                num = int(dartResult[i:i + 2])
                k = mul[dartResult[i + 2]]
                i += 3
                
            else:
                num = int(dartResult[i])
                k = mul[dartResult[i + 1]]
                i += 2
                
            v = num ** k
            points.append(v)
            answer += v
            
        else:
            if dartResult[i] == '*':
                if len(points) > 1:
                    answer += points[-2]
                    points[-2] *= 2
                    
                answer += points[-1]
                points[-1] *= 2
            
            else:
                points[-1] *= -1
                answer += points[-1] * 2
            
            i += 1
            
    return answer
