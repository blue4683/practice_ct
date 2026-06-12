def solution(s):
    answer = ''
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    tmp = ''

    for x in s:
        if x.isnumeric():
            answer += x

        else:
            tmp += x
            if tmp in d:
                answer += d[tmp]
                tmp = ''

    return int(answer)
