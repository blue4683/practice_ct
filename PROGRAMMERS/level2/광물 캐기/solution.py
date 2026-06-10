def solution(picks, minerals):
    answer = 0
    n = len(minerals)
    d = {'diamond': 31, 'iron': 6, 'stone': 1}
    stamina = [{31: 1, 6: 1, 1: 1}, {31: 5, 6: 1, 1: 1}, {31: 25, 6: 5, 1: 1}]
    weights = [list(map(lambda x: d[x], minerals[i:i + 5]))
               for i in range(0, min(n, sum(picks) * 5), 5)]
    weights.sort(key=sum)
    for i in range(3):
        while picks[i] and weights:
            for w in weights.pop():
                answer += stamina[i][w]

            picks[i] -= 1

    return answer
