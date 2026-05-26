from itertools import combinations


def solution(n, q, ans):
    answer = 0
    q = list(map(set, q))
    for code in combinations([i for i in range(1, n + 1)], 5):
        for i in range(len(q)):
            if len(set(code) & q[i]) != ans[i]:
                break

        else:
            answer += 1

    return answer
