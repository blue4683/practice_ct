a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = 0
l, r = 0, 0
while l < a or r < b:
    if l == a:
        r += 1
    
    elif r == b:
        l += 1
    
    elif arr1[l] > arr2[r]:
        r += 1
        
    elif arr1[l] < arr2[r]:
        l += 1
        
    else:
        result += 1
        l += 1
        r += 1

print(result)
