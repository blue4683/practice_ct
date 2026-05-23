def solution(a, b, n):
    answer = 0
    while n // a:
        m = n // a
        answer += m * b
        n = (m * b) + (n % a)

    return answer
