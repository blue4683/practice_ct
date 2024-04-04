import sys
input = sys.stdin.readline

k, n = map(int, input().split())
numbers = []
max_number = 0

for _ in range(k):
    number = input().rstrip()
    max_number = max(max_number, int(number))
    numbers.append(number)

for _ in range(n - k):
    numbers.append(str(max_number))

numbers.sort(key=lambda x: x * 10, reverse=True)
print(int(''.join(numbers)))
