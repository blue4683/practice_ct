n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
nums = {}
for i in range(k):
    if arr[i] in nums:
        nums[arr[i]] += 1
        
    else:
        nums[arr[i]] = 1
    
result = [len(nums.keys())]
while l + k < n:
    nums[arr[l]] -= 1
    if not nums[arr[l]]:
        nums.pop(arr[l])
    
    if arr[l + k] in nums:
        nums[arr[l + k]] += 1
        
    else:
        nums[arr[l + k]] = 1
        
    result.append(len(nums.keys()))
    l += 1
    
print(*result)
