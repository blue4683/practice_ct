import sys
input = sys.stdin.readline

k, l = map(int, input().split())
q = {}
for i in range(1, l + 1):
    q[input().rstrip()] = i

for i, (student, _) in enumerate(sorted(q.items(), key=lambda x: x[1])):
    if i == k:
        break

    print(student)
