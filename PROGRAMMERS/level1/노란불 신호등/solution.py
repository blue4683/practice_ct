def get_gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return get_gcd(b, a % b)


def solution(signals):
    answer = -1
    n = len(signals)
    s = max([signal[0] for signal in signals])
    ys = [signal[0] + 1 for signal in signals]
    ts = [sum(signal) for signal in signals]
    total_t = ts[0]
    for i in range(1, n):
        total_t = total_t * ts[i] // get_gcd(total_t, ts[i])

    for t in range(s, total_t + 1):
        for i in range(n):
            if 0 <= (t % ts[i]) - ys[i] < signals[i][1]:
                continue

            break

        else:
            answer = t
            break

    return answer
