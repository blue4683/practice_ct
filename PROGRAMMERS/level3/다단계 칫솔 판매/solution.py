from collections import deque


class Person:
    def __init__(self, name, referral_name):
        self.name = name
        self.referral_name = referral_name
        self.total = 0
        self.profit = 0

    def set_profit(self, amount):
        self.profit += amount * 100

    def distribute(self, data, profit=0):
        if self.profit:
            distribution = int(self.profit * 0.1)
            self.profit -= distribution
            self.total += self.profit
            self.profit = 0
            if self.referral_name != '-':
                data[self.referral_name].distribute(data, distribution)

        if profit:
            distribution = int(profit * 0.1)
            profit -= distribution
            self.total += profit
            if self.referral_name != '-':
                data[self.referral_name].distribute(data, distribution)


def solution(enroll, referral, seller, amount):
    answer = []
    data = dict()

    data['-'] = Person('-', '--')

    for e, r in zip(enroll, referral):
        data[e] = Person(e, r)

    for name, cnt in zip(seller, amount):
        enr = data[name]
        enr.set_profit(cnt)
        enr.distribute(data)

    for name in enroll:
        answer.append(data[name].total)

    return answer
