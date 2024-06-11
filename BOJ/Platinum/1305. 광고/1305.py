import sys
input = sys.stdin.readline

l = int(input())
string = input().rstrip()
table = [0] * (l + 1)

i = 0
for j in range(1, l):
    while i > 0 and string[i] != string[j]:
        i = table[i - 1]

    if string[i] == string[j]:
        i += 1
        table[j] = i

print(l - table[l - 1])
