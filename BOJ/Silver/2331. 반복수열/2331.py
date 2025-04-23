import sys
input = sys.stdin.readline


a, p = map(int, input().split())
arr = [str(a)]
nums = set([str(a)])
i = 1
result = 0
while 1:
    num = str(sum(map(lambda x: int(x) ** p, list(arr[i - 1]))))
    if num in nums:
        result = arr.index(num)
        break

    nums.add(num)
    arr.append(num)
    i += 1

print(result)
