import sys
input = sys.stdin.readline

n = int(input())
target = [0] * 26
for alp in input().rstrip():
    index = ord(alp) - ord('A')
    target[index] += 1

result = 0
words = [input().rstrip() for _ in range(n - 1)]
for word in words:
    table = [0] * 26
    for alp in word:
        index = ord(alp) - ord('A')
        table[index] += 1

    table = list(map(lambda x, y: x - y, target, table))
    tmp = 0
    flag = 0
    for value in table:
        if not value:
            continue

        if abs(value) != 1:
            break

        else:
            if not flag and not tmp:
                tmp = value

            else:
                tmp += value
                if tmp:
                    break

                flag = 1

    else:
        result += 1


print(result)
