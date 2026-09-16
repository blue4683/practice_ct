n, m = map(int, input().split())
degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1
    
num, max_degree, total = 0, -1, 0
for i in range(1, n + 1):
    total += degree[i]
    if degree[i] > max_degree:
        num, max_degree = i, degree[i]
        
print(num, max_degree)
print(total)
