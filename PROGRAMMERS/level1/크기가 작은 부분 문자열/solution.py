def solution(t, p):
    answer = 0
    n, k = len(t), len(p)
    p = int(p)
    for i in range(n - k + 1):
        target = int(t[i:i + k])
        if target <= p:
            answer += 1

    return answer
