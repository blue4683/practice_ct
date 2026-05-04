def solution(n, m, section):
    answer = 0
    now = 0
    for x in section:
        if x > now:
            answer += 1
            now = x + m - 1

    return answer
