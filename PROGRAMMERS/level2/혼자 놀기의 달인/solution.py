def solution(cards):
    answer = 0
    box = []
    n = len(cards)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i]:
            continue

        cnt, x = 0, i
        while not visited[x]:
            visited[x] = 1
            cnt += 1
            x = cards[x - 1]

        box.append(cnt)

    box.sort()
    answer = box[-1] * box[-2] if len(box) >= 2 else 0
    return answer
