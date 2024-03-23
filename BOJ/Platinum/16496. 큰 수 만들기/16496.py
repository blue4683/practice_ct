import sys
input = sys.stdin.readline

n = int(input())
numbers = list(input().rstrip().split())
max_length = max(map(lambda x: len(x), numbers)) * 2
numbers.sort(key=lambda x: x * max_length, reverse=True)

result = ''.join(numbers)

print(int(result))
