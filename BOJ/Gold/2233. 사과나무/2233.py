import sys
input = sys.stdin.readline


n = int(input())
arr = input().rstrip()
x, y = map(int, input().split())

parent = [0] * (n * 2)
depth = [0] * (n * 2)
index = [0] * (n * 2)
num, node = 0, 0
for i in range(n * 2):
    if arr[i] == '0':
        num += 1
        parent[num] = node
        depth[num] = depth[node] + 1
        node = num
        index[i] = num

    else:
        index[i] = node
        node = parent[node]

x, y = index[x - 1], index[y - 1]
while parent[x] != parent[y]:
    if depth[x] < depth[y]:
        x, y = y, x

    x = parent[x]

target = x if x == y else parent[x]
result = []
for i in range(2 * n):
    if index[i] == target:
        result.append(i + 1)

print(*result)
