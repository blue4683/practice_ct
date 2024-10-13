import sys
input = sys.stdin.readline

def is_alphabet(op):
    if 0 <= ord(op) - ord('A') <= 26:
        return ord(op) - ord('A')
    
    return -1


def calculate(a, b, op):
    if op == '+':
        return a + b
    
    elif op == '-':
        return a - b
    
    elif op == '*':
        return a * b
    
    return a / b


n = int(input())
string = list(input().rstrip())
numbers = [int(input()) for _ in range(n)]
stack = []
for op in string:
    if is_alphabet(op) != -1:
        stack.append(numbers[is_alphabet(op)])

    else:
        b, a = stack.pop(), stack.pop()
        stack.append(calculate(a, b, op))

print(f'{stack[-1]:.2f}')
