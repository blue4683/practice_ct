import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))

result = 0
for num1, num2 in zip(a, b):
    result += num1 * num2

print(result)
