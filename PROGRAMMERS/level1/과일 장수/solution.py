def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    n = len(score)
    for i in range(0, n, m):
        if i + m <= n:
            answer += score[i + m - 1] * m

    return answer
