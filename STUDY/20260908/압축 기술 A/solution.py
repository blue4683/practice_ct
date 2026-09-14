n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = []
l = 0
v = sum(arr[l:l + k])
while l + k <= n:
    if not result:
        result.append(v)
        
    else:
        v = v - arr[l - 1] + arr[l + k - 1]
        if v <= result[-1]:
            result.append(v)
            
    l += 1
    
print(len(result))
print(*result)
