def get_time(time):
    m, s = map(int, time.split(':'))
    return m * 60 + s


def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x: -get_time(x[1]))
    t = get_time(plans[-1][1])
    stack.append(plans.pop())
    while plans:
        name, start, playtime = plans.pop()
        dt = get_time(start) - t
        while stack and dt >= int(stack[-1][2]):
            dt -= int(stack[-1][2])
            answer.append(stack.pop()[0])

        if stack:
            stack[-1][2] = str(int(stack[-1][2]) - dt)

        stack.append([name, start, playtime])
        t = get_time(stack[-1][1])

    while stack:
        answer.append(stack.pop()[0])

    return answer
