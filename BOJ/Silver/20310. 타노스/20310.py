import sys
input = sys.stdin.readline

string = list(input().rstrip())
n = len(string)
zero = string.count('0')
one = n - zero

cnt = 0
for i in range(n):
    if cnt == one // 2:
        break

    if string[i] == '1':
        cnt += 1
        string[i] = ''

cnt = 0
for i in range(n - 1, -1, -1):
    if cnt == zero // 2:
        break

    if string[i] == '0':
        cnt += 1
        string[i] = ''

print(''.join(string))
