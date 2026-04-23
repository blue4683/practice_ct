def convert_time(time):
    tmp = list(map(int, time.split(":")))
    return tmp[0] * 60 + tmp[1]


def fill(time):
    return str(time).zfill(2)


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len, pos, op_start, op_end = map(
        convert_time, [video_len, pos, op_start, op_end])
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end

        if command == 'prev':
            pos = pos - 10 if pos >= 10 else 0

        elif command == 'next':
            pos = pos + 10 if pos + 10 <= video_len else video_len

    if op_start <= pos <= op_end:
        pos = op_end

    answer = f'{fill(pos // 60)}:{fill(pos % 60)}'
    return answer
