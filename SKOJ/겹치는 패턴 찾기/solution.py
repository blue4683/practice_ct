t, p = input().rstrip(), input().rstrip()

n, m = len(t), len(p)
pi = [0] * m
j = 0

for i in range(1, m):
    while j > 0 and p[i] != p[j]:
        j = pi[j - 1]
        
    if p[i] == p[j]:
        j += 1
        pi[i] = j
        
result = 0
point = []

j = 0
for i in range(n):
    while j > 0 and t[i] != p[j]:
        j = pi[j - 1]
        
    if t[i] == p[j]:
        if j == m - 1:
            result += 1
            point.append(i - m + 2)
            j = pi[j]
            
        else:
            j += 1
            
print(result)
print(*point)
