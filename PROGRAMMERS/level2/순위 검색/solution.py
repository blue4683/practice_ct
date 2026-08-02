from bisect import bisect_left
from collections import defaultdict


def solution(info, query):
    answer = []
    options = {
        0: ['cpp', 'java', 'python'],
        1: ['backend', 'frontend'],
        2: ['junior', 'senior'],
        3: ['chicken', 'pizza']
    }
    db = defaultdict(list)
    for h in info:
        key = h.split()
        score = int(key.pop())
        key = tuple(key)
        db[key].append(score)
        db[key].sort()
        
    for q in query:
        q = q.split('and')
        keys = [[], [], [], []]
        for i, opt in enumerate(q[:-1]):
            opt = opt.strip()
            if opt == '-':
                keys[i] = options[i][:]
                
            else:
                keys[i].append(opt)
                
        opt, score = q[-1].split()
        if opt == '-':
            keys[3] = options[3][:]
            
        else:
            keys[3].append(opt)
            
        score = int(score)
        result = 0
        for k1 in keys[0]:
            for k2 in keys[1]:
                for k3 in keys[2]:
                    for k4 in keys[3]:
                        key = (k1, k2, k3, k4)
                        if db[key]:
                            idx = bisect_left(db[key], score)
                            result += len(db[key]) - idx
                        
        answer.append(result)
                
    return answer
