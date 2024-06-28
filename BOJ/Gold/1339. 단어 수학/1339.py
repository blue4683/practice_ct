from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
nums = defaultdict(int)
for string in arr:
    m = len(string)
    for i in range(m):
        s = string[i]
        nums[s] += 10 ** (m - i - 1)

sorted_nums = sorted(nums.items(), key=lambda x: x[1], reverse=True)
result = 0
for i, nums in enumerate(sorted_nums):
    result += nums[1] * (9 - i)

print(result)
