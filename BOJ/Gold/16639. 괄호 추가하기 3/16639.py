from dataclasses import dataclass
import sys
input = sys.stdin.readline


@dataclass
class Value:
    min: int = 0
    max: int = 0


def calculate(start, end):
    result = []
    for i in range(start, end):
        left, right = [dp[start][i].min, dp[start][i].max], [
            dp[i + 1][end].min, dp[i + 1][end].max]
        operator = operators[i]
        for lv in left:
            for rv in right:
                if operator == '+':
                    result.append(lv + rv)

                elif operator == '-':
                    result.append(lv - rv)

                else:
                    result.append(lv * rv)

    return min(result), max(result)


n = int(input()) // 2
expression = input().rstrip()
numbers, operators = [], []
for i, elem in enumerate(expression):
    if i % 2:
        operators.append(elem)

    else:
        numbers.append(int(elem))

dp = [[Value() for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n - i + 1):
        k = i + j
        if k == j:
            dp[j][k].min = numbers[j]
            dp[j][k].max = numbers[j]

        else:
            dp[j][k].min, dp[j][k].max = calculate(j, k)

print(max(dp[0][n].min, dp[0][n].max))
