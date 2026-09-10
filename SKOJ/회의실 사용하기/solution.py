n = int(input())

time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
now = 0
result = 0
for s, e in time:
    if s >= now:
        result += 1
        now = e
        
print(result)
