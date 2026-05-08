def solution(today, terms, privacies):
    answer = []
    time = {}
    for term in terms:
        a, b = term.split()
        time[a] = int(b)

    ty, tm, td = map(int, today.split('.'))
    for i in range(len(privacies)):
        privacy = privacies[i]
        t, a = privacy.split()
        y, m, d = map(int, t.split('.'))
        y += time[a] // 12
        m += time[a] % 12
        d -= 1
        if d == 0:
            d = 28
            m -= 1

        if m > 12:
            y += 1
            m %= 12

        if y < ty or (y == ty and m < tm) or (y == ty and m == tm and d < td):
            answer.append(i + 1)

    return answer
