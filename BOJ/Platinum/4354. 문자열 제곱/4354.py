import sys
input = sys.stdin.readline

while 1:
    string = input().rstrip()
    if string == '.':
        break

    n = len(string)
    table = [0] * n

    i = 0
    for j in range(1, n):
        while i > 0 and string[i] != string[j]:
            i = table[i - 1]

        if string[i] == string[j]:
            i += 1
            table[j] = i

    if n % (n - table[n - 1]):
        print(1)

    else:
        print(n // (n - table[n - 1]))
