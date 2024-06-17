import sys
input = sys.stdin.readline
MAX = 360000

n = int(input())
clock = [0] * (MAX * 2)
for c in map(int, input().split()):
    clock[c] = 1
    clock[c + MAX] = 1

clock *= 2
pattern = [0] * MAX
for c in map(int, input().split()):
    pattern[c] = 1

table = [0] * MAX
i = 0
for j in range(1, MAX):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i - 1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i

result = 0
i = 0
for j in range(1, MAX * 2):
    while i > 0 and pattern[i] != clock[j]:
        i = table[i - 1]

    if pattern[i] == clock[j]:
        if i == MAX - 1:
            result = 1
            break

        else:
            i += 1

print('possible') if result else print('impossible')
