def convert(num, k):
    v = 0
    n = len(num)
    for i in range(n - 1, -1, -1):
        if int(num[i]) >= k:
            return -1

        v += int(num[i]) * (k ** (n - 1 - i))

    return v


def solution(expressions):
    answer = []
    targets = []
    base = [i for i in range(2, 10)]
    for k in base[:]:
        for expression in expressions:
            tmp = expression.split(' ')
            a, b = convert(tmp[0], k), convert(tmp[2], k)
            if -1 in {a, b}:
                base.remove(k)
                break

            elif tmp[4] != 'X':
                c = convert(tmp[4], k)
                if c == -1:
                    base.remove(k)
                    break

                if (tmp[1] == '+' and a + b != c) or (tmp[1] == '-' and a - b != c):
                    base.remove(k)
                    break

    for expression in expressions:
        if 'X' in expression:
            targets.append(expression.split(' '))

    for expression in targets:
        possible = set()
        for k in base:
            a, b = convert(expression[0], k), convert(expression[2], k)
            if expression[1] == '+':
                c = a + b

            else:
                c = a - b

            if not c:
                result = 0

            else:
                result = ''
                while c:
                    result = str(c % k) + result
                    c //= k

            possible.add(result)

        if len(possible) == 1:
            result = possible.pop()

        else:
            result = '?'

        answer.append(
            f'{expression[0]} {expression[1]} {expression[2]} = {result}')

    return answer
