from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pizza = deque(enumerate(map(int, input().split())))
result = [0] * n
second = 0

while pizza:
    second += 1
    index, cnt = pizza.popleft()
    cnt -= 1
    if cnt:
        pizza.append((index, cnt))
        continue

    result[index] = second

print(*result)
