import sys
input = sys.stdin.readline

n = int(input())
villages = [list(map(int, input().split())) for _ in range(n)]
villages.sort()

people = [0] * n
people[0] = villages[0][1]
for i in range(1, n):
    people[i] = people[i - 1] + villages[i][1]

result = 0
for i in range(n):
    if people[i] >= people[-1] - people[i]:
        result = villages[i][0]
        break

print(result)
