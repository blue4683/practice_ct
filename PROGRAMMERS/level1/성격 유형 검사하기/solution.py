from collections import defaultdict


def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    n = len(survey)
    for i in range(n):
        a, b = survey[i]
        c = choices[i]
        if c > 4:
            score[b] += (c - 4)

        elif c < 4:
            score[a] += (4 - c)

    for a, b in ['RT', 'CF', 'JM', 'AN']:
        if score[a] >= score[b]:
            answer += a

        else:
            answer += b

    return answer
