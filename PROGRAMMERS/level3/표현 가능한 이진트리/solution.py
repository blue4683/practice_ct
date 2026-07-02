from collections import deque


def solution(numbers):
    answer = []
    for number in numbers:
        number = bin(number)[2:]
        l = 2
        while l < len(number):
            l *= 2
        
        number = '0' * (l - 1 - len(number)) + number
        q = deque([(len(number) // 2, l // 4)])
        possible = 1
        while q:
            root, gap = q.popleft()
            if not gap:
                break
                
            left, right = root - gap, root + gap
            if number[root] == '0' and (number[left] == '1' or number[right] == '1'):
                possible = 0
                break
                
            q.append((left, gap // 2))
            q.append((right, gap // 2))
        
        answer.append(possible)
        
    return answer
