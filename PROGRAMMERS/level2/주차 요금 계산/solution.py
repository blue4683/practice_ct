from collections import defaultdict


def solution(fees, records):
    answer = []
    parking = defaultdict(int)
    prefix_time = defaultdict(int)
    for record in records:
        time, num, in_out = record.split()
        h, m = map(int, time.split(':'))
        time = 60 * h + m
        if in_out == 'IN':
            parking[num] = time

        else:
            prefix_time[num] += time - parking[num]
            parking[num] = -1

    for num in parking:
        if parking[num] != -1:
            prefix_time[num] += 24 * 60 - 1 - parking[num]
            parking[num] = -1

    for num in sorted(prefix_time.keys()):
        time = prefix_time[num]
        if time <= fees[0]:
            answer.append(fees[1])

        else:
            answer.append(fees[1] + (((time - fees[0]) // fees[2]) +
                          int(((time - fees[0]) % fees[2]) > 0)) * fees[3])

    return answer
