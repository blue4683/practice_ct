import sys
input = sys.stdin.readline

s = input().rstrip()
arr = []
for i in range(len(s)):
    arr.append(s[i:])

arr.sort()
for string in arr:
    print(string)
