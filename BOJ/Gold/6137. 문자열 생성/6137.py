import sys
input = sys.stdin.readline

n = int(input())
s = [input().rstrip() for _ in range(n)]
start, end = 0, n - 1
t = ''

while start <= end:
    if start == end or ord(s[start]) < ord(s[end]):
        t += s[start]
        start += 1

    elif ord(s[start]) > ord(s[end]):
        t += s[end]
        end -= 1

    else:
        ns, ne = start + 1, end - 1
        while ord(s[ns]) == ord(s[ne]) and ns < ne:
            ns += 1
            ne -= 1

        if ord(s[ns]) <= ord(s[ne]):
            t += s[start]
            start += 1

        else:
            t += s[end]
            end -= 1

    if len(t) == 80:
        print(t)
        t = ''

if t != '':
    print(t)
