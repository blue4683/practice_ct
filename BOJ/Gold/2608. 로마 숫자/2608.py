import sys
input = sys.stdin.readline

num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convert_to_num(string: str) -> int:
    result = 0
    n = len(string)
    nine = -1

    for i in range(n):
        if i == nine:
            continue

        if i != n - 1 and num_dict[string[i]] < num_dict[string[i + 1]]:
            nine = i + 1
            result += num_dict[string[i + 1]] - num_dict[string[i]]

        else:
            result += num_dict[string[i]]

    return result


def convert_to_str(num: int) -> str:
    result = ''
    arr = sorted(num_dict.items(), key=lambda x: -x[1])
    n = len(arr)

    for i in range(0, n, 2):
        string, mod = arr[i]
        cnt = num // mod
        if cnt < 5:
            if cnt == 4:
                result += string + arr[i - 1][0]

            else:
                result += string * cnt

        else:
            if cnt == 9:
                result += string + arr[i - 2][0]

            else:
                result += arr[i - 1][0] + string * (cnt % 5)

        num %= mod

    return result


a, b = [input().rstrip() for _ in range(2)]
result = convert_to_num(a) + convert_to_num(b)
print(result)
print(convert_to_str(result))
