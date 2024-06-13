import sys
input = sys.stdin.readline

string = input().rstrip().split(':')
n = len(string)

if n != 8:
    i = string.index('')
    string = string[:i] + [''] * (8 - n + 1) + string[i + 1:]
    n = 8

for i in range(n):
    string[i] = string[i].zfill(4)

print(':'.join(string))
