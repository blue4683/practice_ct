a, b, s = map(int, input().split())

result = 0
for num in range(a, b + 1):
    if sum(map(int, list(str(num)))) == s:
        result += 1
        
print(result)
