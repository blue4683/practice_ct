from itertools import product


def solution(users, emoticons):
    answer = []
    n = len(emoticons)
    pcts = product(*[range(1, 5) for _ in range(n)])
    for pct in pcts:
        cnt, price = 0, 0
        for k, limit in users:
            v = 0
            for emoticon, p in zip(emoticons, pct):
                if p * 10 >= k:
                    v += (emoticon * (10 - p)) // 10

            if v >= limit:
                cnt += 1
                
            else:
                price += v
        
        if [cnt, price] > answer:
            answer = [cnt, price]
            
    return answer
