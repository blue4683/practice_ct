def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]
    l, v = 0, 0
    for r in range(n):
        v += sequence[r]
        while v > k:
            v -= sequence[l]
            l += 1

        if v == k:
            if answer[1] - answer[0] > r - l or answer[1] - answer[0] == r - l and l < answer[0]:
                answer = [l, r]

    return answer
