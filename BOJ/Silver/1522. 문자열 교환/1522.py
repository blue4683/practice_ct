import sys
input = sys.stdin.readline

string = input().rstrip()
cnt = string.count('a')

string += string[:cnt - 1]
result = 10 ** 9
for i in range(len(string) - (cnt - 1)):
    result = min(result, string[i:i + cnt].count('b'))

print(result)
