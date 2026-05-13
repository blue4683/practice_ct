def solution(number, limit, power):
    answer = 0
    weapons = []
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if not i % j:
                cnt += 1
                if i // j != j:
                    cnt += 1

        weapons.append(power if cnt > limit else cnt)

    answer = sum(weapons)
    return answer
