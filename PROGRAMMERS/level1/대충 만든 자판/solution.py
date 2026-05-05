def solution(keymap, targets):
    answer = []
    cnt = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in cnt:
                cnt[key[i]] = i + 1

            else:
                cnt[key[i]] = min(cnt[key[i]], i + 1)

    for target in targets:
        tmp = 0
        for alp in target:
            if alp not in cnt:
                tmp = -1
                break

            tmp += cnt[alp]

        answer.append(tmp)

    return answer
