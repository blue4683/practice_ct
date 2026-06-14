def solution(lottos, win_nums):
    answer = []
    cnt = lottos.count(0)
    remain = set(win_nums) - set(lottos)
    win = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    answer.append(win[6 - (len(remain) - cnt)])
    answer.append(win[6 - len(remain)])
    return answer
