def solution(brown, yellow):
    answer = []
    n=brown+yellow
    for i in range(3,n//2+1):
        if not n%i:
            if (i-2)*(n//i-2)==yellow:
                answer+=sorted([i,n//i],reverse=True)
                break
    return answer