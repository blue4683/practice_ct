import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

result = 10 ** 9
left, right = 0, n - 1
while left < right:
    liquid = arr[left] + arr[right]
    if abs(liquid) < abs(result):
        result = liquid

    if liquid > 0:
        right -= 1

    else:
        left += 1

print(result)
