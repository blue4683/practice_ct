from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
scores = [tuple(map(int, input().split())) for _ in range(n)]

result = 0
for order in permutations(range(1, 9)):
    order = [*order, 0]
    s, num = 0, 4
    for score in scores:
        base = [0] * 3
        out = 0
        while out < 3:
            num = (num + 1) % 9
            player = order[num]
            hit = score[player]
            if hit == 0:
                out += 1

            elif hit == 1:
                s += base[2]
                base = [1] + base[:2]

            elif hit == 2:
                s += base[2] + base[1]
                base = [0, 1, base[0]]

            elif hit == 3:
                s += base[2] + base[1] + base[0]
                base = [0, 0, 1]

            elif hit == 4:
                s += base[2] + base[1] + base[0] + 1
                base = [0, 0, 0]

    if result < s:
        result = s

print(result)
