import sys
input = sys.stdin.readline

n = int(input())
snow = sorted(list(map(int, input().split())))

result = 10 ** 9
for i in range(n):
    for j in range(i, n):
        a = snow[i] + snow[j]
        left, right = i + 1, j - 1
        while left < right:
            b = snow[left] + snow[right]
            result = min(result, abs(b - a))
            if b > a:
                right -= 1

            else:
                left += 1

print(result)
