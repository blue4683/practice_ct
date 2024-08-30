import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

before_cost = 10 ** 9
result = 0

for distance, cost in zip(distances, costs[:-1]):
    if cost < before_cost:
        before_cost = cost

    result += before_cost * distance

print(result)
