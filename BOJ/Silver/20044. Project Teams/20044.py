import sys
input = sys.stdin.readline

n = int(input())
students = sorted(list(map(int, input().split())))

result = 200000
for i in range(n):
    result = min(result, students[i] + students[-(i + 1)])

print(result)
