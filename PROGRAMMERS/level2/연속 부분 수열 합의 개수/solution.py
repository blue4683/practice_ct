def solution(elements):
    answer = set(elements)
    n = len(elements)
    elements += elements
    for l in range(2, n + 1):
        r = l
        v = sum(elements[:r])
        while r < 2 * n - 1:
            v -= elements[r - l]
            v += elements[r]
            r += 1
            answer.add(v)

    return len(answer)
