def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)

    def check(level):
        t = 0
        for i in range(n):
            diff = diffs[i]
            k = 0 if level >= diff else diff - level
            t += k * (times[i - 1] + times[i]) + times[i]

        return t <= limit

    l, r = 1, max(diffs)
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1

        else:
            l = mid + 1

    answer = l
    return answer
