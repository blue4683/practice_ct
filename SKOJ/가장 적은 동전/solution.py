n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n - 1, -1, -1):
    if not k:
        break
    
    v = arr[i]
    result += k // v
    k %= v

print(result)
