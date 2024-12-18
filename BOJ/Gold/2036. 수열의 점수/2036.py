import sys
input = sys.stdin.readline

n = int(input())
minus, zero, plus = [], [], []
for _ in range(n):
    num = int(input())
    if num < 0:
        minus.append(num)

    elif num > 0:
        plus.append(num)

    else:
        zero.append(num)

minus.sort(reverse=True)
plus.sort()

result = 0
while plus:
    a = plus.pop()
    b = plus.pop() if plus else 0
    if b <= 1:
        result += a + b

    else:
        result += a * b

while minus:
    a = minus.pop()
    b = minus.pop() if minus else 0
    if not b:
        if zero:
            zero.pop()

        else:
            result += a

    else:
        result += a * b

print(result)
