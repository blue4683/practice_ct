def get_time(t):
    return 60 * (t // 100) + (t % 100)


def solution(schedules, timelogs, startday):
    answer = 0
    schedules = list(map(get_time, schedules))
    n = len(schedules)
    for i in range(n):
        for j in range(7):
            today = startday + j
            t = today % 8 + today // 8
            if t >= 6:
                continue

            time = get_time(timelogs[i][j])
            if time - schedules[i] > 10:
                break

        else:
            answer += 1

    return answer
