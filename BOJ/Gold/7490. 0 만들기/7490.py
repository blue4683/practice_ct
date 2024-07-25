import sys
input = sys.stdin.readline

d = [' ', '+', '-']


def calculate(modulars, nums):
    expression = '1'
    remove_blank_nums = [1]
    remove_blank_modulars = []
    for modular, num in zip(modulars, nums):
        expression += modular + str(num)
        if modular == ' ':
            remove_blank_nums[-1] = int(str(remove_blank_nums[-1]) + str(num))

        else:
            remove_blank_nums.append(num)
            remove_blank_modulars.append(modular)

    value = remove_blank_nums[0]
    for modular, num in zip(remove_blank_modulars, remove_blank_nums[1:]):
        if modular == '+':
            value += num

        else:
            value -= num

    return value, expression


def dfs(depth, modulars, nums):
    global result
    if depth == n + 1:
        value, expression = calculate(modulars, nums)
        if not value:
            result.append(expression)

        return

    for modular in d:
        modulars.append(modular)
        nums.append(depth)
        dfs(depth + 1, modulars, nums)
        nums.pop()
        modulars.pop()


for _ in range(int(input())):
    n = int(input())
    result = []
    dfs(2, [], [])
    for expression in result:
        print(expression)

    print()
