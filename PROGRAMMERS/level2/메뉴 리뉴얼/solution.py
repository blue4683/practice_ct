from collections import Counter, defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        cook = defaultdict(int)
        for order in orders:
            if len(order) < n:
                continue
                
            for comb in combinations(sorted(order), n):
                cook[comb] += 1
                
        counter = Counter(cook).most_common()
        if not counter:
            continue

        mx = counter[0][1]
        if mx < 2:
            continue
            
        for comb, cnt in counter:
            if cnt != mx:
                break
                
            answer.append(''.join(comb))
    
    answer.sort()
    return answer
