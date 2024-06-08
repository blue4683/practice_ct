import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []
for s in string:
    stack.append(s)
    if stack[-4:] == list('PPAP'):
        for _ in range(4):
            stack.pop()

        stack.append('P')

if stack == list('PPAP') or stack == ['P']:
    print('PPAP')

else:
    print('NP')
