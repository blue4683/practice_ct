def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        idx = 0
        prev = ''
        while idx < len(word):
            speak = 1
            for t in words:
                if t == prev:
                    continue

                if word[idx:idx + len(t)] == t:
                    idx += len(t)
                    prev = t
                    break

            else:
                speak = 0
                break

        if speak:
            answer += 1

    return answer
