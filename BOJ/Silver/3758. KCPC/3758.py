import sys
input = sys.stdin.readline


class Team:
    def __init__(self):
        self.score = [0] * (k + 1)
        self.submit_cnt = 0
        self.last_submit = 0


for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    teams = [Team() for _ in range(n + 1)]
    for log_idx in range(1, m + 1):
        i, j, s = map(int, input().split())
        team = teams[i]
        team.score[j] = max(team.score[j], s)
        team.submit_cnt += 1
        team.last_submit = log_idx

    result = []
    for i in range(1, n + 1):
        team = teams[i]
        result.append(
            (sum(team.score), -team.submit_cnt, -team.last_submit, i))

    result.sort(reverse=True)
    for i in range(n):
        if result[i][-1] == t:
            print(i + 1)
            break
