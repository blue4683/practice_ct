def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        j = int(i ** 0.5)
        if j * j == i:
            answer -= i

        else:
            answer += i

    return answer
