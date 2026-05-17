def solution(ingredient):
    answer = 0
    stack, bread = [], 0
    for i in ingredient:
        if i == 1 and stack and stack[-1] != 1 and bread > 0:
            burger = []
            while stack and stack[-1] != 1:
                burger.append(stack.pop())

            burger.append(stack.pop())
            if burger == [3, 2, 1]:
                answer += 1
                bread -= 1

            else:
                while burger:
                    stack.append(burger.pop())

                stack.append(i)
                bread += 1

        else:
            stack.append(i)
            bread += 1 if i == 1 else 0

    return answer
