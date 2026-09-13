n, q = map(int, input().split())
arr = list(map(int, input().split()))

cache = {}
for num in [int(input()) for _ in range(q)]:
    if num not in cache:
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < num:
                l = mid + 1
                
            elif arr[mid] > num:
                r = mid - 1
                
            else:
                cache[num] = 1
                break
        
        else:
            cache[num] = 0
    
    print(cache[num])
