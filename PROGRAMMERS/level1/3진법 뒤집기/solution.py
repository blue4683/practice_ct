def solution(n):
    answer = 0
    num = ''
    while n:
        num += str(n % 3)
        n //= 3

    l = len(num)
    for i in range(l):
        answer += int(num[i]) * 3 ** (l - 1 - i)

    return answer
