import sys
input = sys.stdin.readline

while 1:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break

    set_arr = set(arr)
    if len(set_arr) == 1:
        print('Equilateral')

    else:
        arr.sort()
        if arr[-1] < sum(arr[:2]):
            if len(set_arr) == 2:
                print('Isosceles')

            else:
                print('Scalene')

        else:
            print('Invalid')
