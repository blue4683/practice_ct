def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a, b = i // n + 1, i % n + 1
        answer.append(max(a, b))
        
    return answer
