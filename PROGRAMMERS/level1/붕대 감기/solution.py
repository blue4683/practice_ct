def solution(bandage, health, attacks):
    answer = 0
    n = len(attacks)
    now, t, idx, duration = health, 0, 0, 0
    while idx < n and now > 0:
        t += 1
        if attacks[idx][0] == t:
            now -= attacks[idx][1]
            idx += 1
            duration = 0

        else:
            if now < health:
                now = now + bandage[1] if now + \
                    bandage[1] <= health else health

            duration += 1
            if not (duration % bandage[0]):
                now = now + bandage[2] if now + \
                    bandage[2] <= health else health
                duration = 0

    answer = now if now > 0 else -1
    return answer
