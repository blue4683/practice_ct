for testcase in range(1, int(input())+1):
    case = list(input())
    stick = 0
    result = 0
    idx = 0
    while idx<len(case):
        if case[idx]=='(':
            stick += 1
        else:
            if case[idx-1]=='(':
                stick -= 1
                result += stick
            else:
                result += 1
                stick -= 1
        idx += 1
    print(f'#{testcase} {result}')