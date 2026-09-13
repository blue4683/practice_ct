n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
result = sum(arr[l:l + k])
v = result
while l + k < n:
    v -= arr[l]
    v += arr[l + k]
    result = max(result, v)
    l += 1
    
print(result)
