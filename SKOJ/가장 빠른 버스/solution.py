n, q = map(int, input().split())
arr = list(map(int, input().split()))

result = {}
for a in [int(input()) for _ in range(q)]:
    if a in result:
        print(result[a])
        continue
    
    if a > arr[-1]:
        result[a] = -1
        
    else:
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if a <= arr[mid]:
                r = mid - 1
                
            else:
                l = mid + 1
                
        result[a] = arr[l]
        
    print(result[a])
