def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for s in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(s, '')

    while 1:
        tmp = new_id.replace('..', '.')
        if tmp == new_id:
            break

        new_id = tmp

    if new_id != '' and new_id[0] == '.':
        new_id = new_id[1:]

    if new_id != '' and new_id[-1] == '.':
        new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    answer = new_id
    return answer
