def solution(numbers, hand):
    answer = ''
    pos = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }

    l, r = '*', '#'

    def get_dist(a, b):
        y1, x1 = pos[a]
        y2, x2 = pos[b]
        return abs(y1 - y2) + abs(x1 - x2)

    for number in numbers:
        if number in {1, 4, 7}:
            answer += 'L'
            l = str(number)

        elif number in {3, 6, 9}:
            answer += 'R'
            r = str(number)

        else:
            number = str(number)
            a, b = get_dist(number, l), get_dist(number, r)
            if a < b or (a == b and hand == 'left'):
                answer += 'L'
                l = number

            elif a > b or (a == b and hand == 'right'):
                answer += 'R'
                r = number

    return answer
