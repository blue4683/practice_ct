import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
n, m = map(len, [s, p])

result = 0
idx = 0
k = n
while idx < m:
    if p[idx: idx + k] not in s:
        k -= 1

    else:
        result += 1
        idx += k
        k = n

print(result)
