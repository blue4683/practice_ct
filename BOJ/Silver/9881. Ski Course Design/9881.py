import sys
input = sys.stdin.readline


def get_cost(lowest, highest):
    cost = 0
    for hill in hills:
        if hill < lowest:
            cost += (lowest - hill) ** 2

        elif highest - hill > 17:
            cost += (highest - hill - 17) ** 2

        elif hill - lowest > 17:
            cost += (hill - lowest - 17) ** 2

        elif hill > highest:
            cost += (hill - highest) ** 2

    return cost


n = int(input())
hills = sorted([int(input()) for _ in range(n)])
if hills[-1] - hills[0] <= 17:
    print(0)
    sys.exit()

result = 10 ** 9
lowest = hills[0]
highest = hills[-1]

while lowest < highest:
    result = min(result, get_cost(lowest, lowest + 17))
    lowest += 1

print(result)
