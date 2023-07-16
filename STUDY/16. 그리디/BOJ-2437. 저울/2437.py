import sys
input=sys.stdin.readline

def find_range(nums):
    global result
    for num in nums:
        if result<num: break
        result+=num
    return result

n=int(input())
nums=sorted(list(map(int,input().split())))
result=1

print(find_range(nums))