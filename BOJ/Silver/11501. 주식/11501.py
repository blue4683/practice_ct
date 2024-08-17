import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stacks = list(map(int, input().split()))
    result = 0
    max_price = 0

    for price in stacks[::-1]:
        if price > max_price:
            max_price = price

        else:
            result += max_price - price

    print(result)
