def solution(n, k):
    answer = 0
    num = ''
    if k != 10:
        while n:
            num = str(n % k) + num
            n //= k
            
    else:
        num = str(n)

    num = list(map(lambda x: int(x) if x != '' else 0, num.split('0')))
    for x in num:
        if x < 2 or x > 2 and not x % 2:
            continue
            
        i = 3
        while i * i <= x:
            if not x % i:
                break
                
            i += 2
        
        else:
            answer += 1
        
    return answer
