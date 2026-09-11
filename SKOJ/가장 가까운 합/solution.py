n, t = map(int, input().split())
arr = list(map(int, input().split()))

result, diff = 10 ** 9, 10 ** 9
for i in range(n):
    for j in range(i + 1, n):
        k = arr[i] + arr[j]
        tmp = abs(t - k)
        if tmp < abs(diff):
            result = k
            diff = tmp
        
        elif tmp == abs(diff):
            result = min(result, k)    

print(result)            
