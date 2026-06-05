from math import ceil, floor


def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        if x < r1:
            answer += floor((r2 * r2 - x * x) ** 0.5) - \
                ceil((r1 * r1 - x * x) ** 0.5) + 1

        else:
            answer += floor((r2 * r2 - x * x) ** 0.5) + 1

    answer *= 4
    return answer
