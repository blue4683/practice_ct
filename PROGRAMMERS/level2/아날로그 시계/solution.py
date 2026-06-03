def solution(h1, m1, s1, h2, m2, s2):
    answer = -1
    s = h1 * 3600 + m1 * 60 + s1
    e = h2 * 3600 + m2 * 60 + s2
    if e <= s:
        e += 12 * 3600

    def count(time):
        minute = (time * 59) // 3600
        hour = (time * 719) // 43200
        duplicate = time // 43200
        return minute + hour - duplicate

    answer = count(e) - count(s)
    if not (s * 59) % 3600 or not (s * 719) % 43200:
        answer += 1

    return answer
