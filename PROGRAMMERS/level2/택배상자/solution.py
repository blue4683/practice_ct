def solution(order):
    answer = 0
    n = len(order) + 1
    stack = []
    for i in range(1, n):
        if order[answer] != i:
            stack.append(i)

        else:
            answer += 1

        while stack and stack[-1] == order[answer]:
            answer += 1
            stack.pop()

    return answer
