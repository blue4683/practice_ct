def solution(queue1, queue2):
    answer = 0
    s = sum(queue1) + sum(queue2)
    if s % 2:
        return -1

    q = queue1 + queue2
    t, cur = s // 2, sum(queue1)
    l, r = 0, len(queue1)
    while l < r <= len(q):
        if cur > t:
            cur -= q[l]
            l += 1
            answer += 1

        elif cur < t:
            if r < len(q):
                cur += q[r]
                r += 1
                answer += 1

            else:
                return -1

        else:
            return answer

    return -1
