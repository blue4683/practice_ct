from collections import defaultdict

def solution(gems):
    answer = []
    n = len(gems)
    end = 0
    unique_gems = set(gems)
    data = defaultdict(int)
    
    cases = []
    
    for start, gem in enumerate(gems):
        while len(data) < len(unique_gems) and end < n:
            data[gems[end]] += 1
            end += 1
            
        if len(data) == len(unique_gems):
            cases.append([start + 1, end])
            
        data[gem] -= 1
        if not data[gem]:
            del(data[gem])
            
    cases.sort(key=lambda x:x[1] - x[0])
    answer = cases[0]
    
    return answer