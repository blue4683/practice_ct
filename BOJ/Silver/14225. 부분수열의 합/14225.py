import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
nums = set()
for bit in range(1, 1 << n):
    num = 0
    for i in range(n):
        if bit & (1 << i):
            num += s[i]

    nums.add(num)

result = 1
while result in nums:
    result += 1

print(result)
