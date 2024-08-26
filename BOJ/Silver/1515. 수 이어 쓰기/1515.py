import sys
input = sys.stdin.readline


def solution():
    number = input().rstrip()
    last = 0

    for i in range(1, 30000):
        num = str(i)
        for j in range(len(num)):
            if num[j] == number[last]:
                last += 1

            if last == len(number):
                print(i)
                return


if __name__ == '__main__':
    solution()
