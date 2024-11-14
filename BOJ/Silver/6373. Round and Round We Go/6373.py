import sys
input = sys.stdin.readline


def check(a, b):
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return 1

    return 0


while 1:
    try:
        string = input().rstrip()
        number = int(string)
        n = len(string)
        result = 'not cyclic'
        for i in range(2, n + 1):
            tmp_string = str(number * i).zfill(n)
            if len(tmp_string) != n or not check(string, tmp_string):
                break

        else:
            result = 'cyclic'

        print(f'{string} is {result}')

    except:
        break
