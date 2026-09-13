n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = -1
l, r = 0, n - 1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] < x:
        l = mid + 1
        
    elif arr[mid] > x:
        r = mid - 1
        
    else:
        result = mid
        break

while result > 0 and arr[result - 1] == x:
    result -= 1
    
print(result)
