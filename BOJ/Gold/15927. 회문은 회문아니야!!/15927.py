import sys
input = sys.stdin.readline

string = input().rstrip()
n = len(string)
result = -1

if string == string[::-1]:
    if string != string[0] * n:
        result = n - 1

else:
    result = n

print(result)
