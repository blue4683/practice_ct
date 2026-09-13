n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[-1])

result = 0
t = 0
for s, e in arr:
    if t <= s:
        result += 1
        t = e
        
print(result)
