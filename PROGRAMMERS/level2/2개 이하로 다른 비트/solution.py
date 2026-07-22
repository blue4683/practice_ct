from math import log2


def solution(numbers):
    answer = []
    for number in numbers:
        n = int(log2(number)) if number else 0
        for i in range(n + 1):
            if not number & 1 << i:
                answer.append(number + (1 << i))
                break
                
            if number & 1 << i and not number & 1 << i + 1:
                answer.append(number + (1 << i))
                break
        
        else:
            answer.append(number + (1 << n))
                
    return answer
