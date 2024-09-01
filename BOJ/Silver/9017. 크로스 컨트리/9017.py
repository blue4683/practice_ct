import sys
input = sys.stdin.readline


class Team:
    def __init__(self, num):
        self.num = num
        self.score = 0
        self.member_count = 0
        self.last_member_rank = 0


for _ in range(int(input())):
    n = int(input())
    ranks = list(map(int, input().split()))
    possible = set(ranks)
    possible = set(num for num in possible if ranks.count(num) == 6)
    teams = {num: Team(num) for num in possible}
    teams[0] = Team(0)
    teams[0].score = 10 ** 6

    rank = 1
    for num in ranks:
        if num not in teams:
            continue

        team = teams[num]
        if team.member_count < 4:
            team.score += rank

        if team.member_count < 5:
            team.last_member_rank = rank

        team.member_count += 1
        rank += 1

    result = teams[0]
    for num in teams:
        team = teams[num]
        if team.score < result.score:
            result = team
            continue

        if team.score == result.score and team.last_member_rank < result.last_member_rank:
            result = team

    print(result.num)
