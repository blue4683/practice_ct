def solution(friends, gifts):
    answer = 0
    n = len(friends)
    index = {friends[i]: i for i in range(n)}
    score = [0] * n
    trade = [[0] * n for _ in range(n)]

    for gift in gifts:
        i, j = map(lambda x: index[x], gift.split())
        score[i] += 1
        score[j] -= 1
        trade[i][j] += 1

    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if trade[i][j] or trade[j][i]:
                if trade[i][j] == trade[j][i]:
                    if score[i] == score[j]:
                        continue

                    k = i if score[i] > score[j] else j

                else:
                    k = i if trade[i][j] > trade[j][i] else j

            else:
                if score[i] == score[j]:
                    continue

                k = i if score[i] > score[j] else j

            result[k] += 1

    answer = max(result)
    return answer
