import sys
input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
m = int(input())
students = [tuple(map(int, input().split())) for _ in range(m)]

for gender, index in students:
    if gender % 2:
        for i in range(index - 1, n, index):
            switches[i] ^= 1

    else:
        index -= 1
        start, end = index - 1, index + 1
        while start >= 0 and end <= n - 1:
            if switches[start] != switches[end]:
                break

            start -= 1
            end += 1

        for i in range(start + 1, end):
            switches[i] ^= 1

for i in range(1, n + 1):
    print(switches[i - 1], end=' ')
    if i and not i % 20:
        print()
