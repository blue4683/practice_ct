def ban(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
        
    return True

def find(suspections, banned):
    if not suspections:
        cases.add(tuple(sorted(banned)))
        return
    
    for i in suspections[0]:
        if i not in banned:
            find(suspections[1:], {i} | banned)
    
def solution(user_id, banned_id):
    global cases
    
    cases = set()
    suspections = []
    answer = 0
    
    for banned in banned_id:
        suspections.append([i for i in range(len(user_id)) if ban(user_id[i], banned)])
        
    suspections.sort(key=len)
    
    find(suspections, set())
    answer = len(cases)
    
    return answer