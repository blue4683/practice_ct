import sys
input = sys.stdin.readline
MAX = 50000000
MOD = 2 ** 8


def find_loop():
    skip = {}
    stack = []
    for i, op in enumerate(cmd):
        if op == '[':
            stack.append(i)

        elif op == ']':
            front = stack.pop()
            skip[front] = i
            skip[i] = front

    return skip


for _ in range(int(input())):
    sm, sc, si = map(int, input().split())
    cmd = input().rstrip()
    input_string = list(input().rstrip()[::-1])

    memory = [0] * sm
    memory_ptr, cmd_ptr, loop_ptr, cnt = 0, 0, sc, 0
    skip = find_loop()

    result = []
    while cmd_ptr < sc:
        cnt += 1
        op = cmd[cmd_ptr]
        if op == '-':
            memory[memory_ptr] -= 1
            memory[memory_ptr] %= MOD

        elif op == '+':
            memory[memory_ptr] += 1
            memory[memory_ptr] %= MOD

        elif op == '<':
            memory_ptr -= 1
            memory_ptr %= sm

        elif op == '>':
            memory_ptr += 1
            memory_ptr %= sm

        elif op == '[':
            if not memory[memory_ptr]:
                cmd_ptr = skip[cmd_ptr]

        elif op == ']':
            if memory[memory_ptr]:
                cmd_ptr = skip[cmd_ptr]

        elif op == ',':
            if input_string:
                memory[memory_ptr] = ord(input_string.pop())

            else:
                memory[memory_ptr] = 255

        if cnt > MAX:
            loop_ptr = min(loop_ptr, cmd_ptr)

        cmd_ptr += 1
        if cnt > MAX * 2:
            result = [loop_ptr, skip[loop_ptr]]
            break

    if result:
        a, b = result
        print(f'Loops {a} {b}')

    else:
        print('Terminates')
