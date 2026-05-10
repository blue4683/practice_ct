def solution(s):
    n = len(s)
    answer = [-1] * n
    index = {}
    for i in range(n):
        alp = s[i]
        if alp in index:
            answer[i] = i - index[alp]

        index[alp] = i

    return answer
