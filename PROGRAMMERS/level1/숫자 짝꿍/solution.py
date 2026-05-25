def solution(X, Y):
    answer = ''
    x, y = {str(i): 0 for i in range(10)}, {str(i): 0 for i in range(10)}
    for num in X:
        x[num] += 1

    for num in Y:
        y[num] += 1

    for i in range(9, -1, -1):
        answer += str(i) * min(x[str(i)], y[str(i)])

    if answer == '':
        answer = '-1'

    elif answer[0] == '0':
        answer = '0'

    return answer
