def solution(cards1, cards2, goal):
    answer = 'No'
    n, m, k = map(len, [cards1, cards2, goal])

    def dfs(l, r, t):
        nonlocal answer
        if answer == 'Yes':
            return

        if t == k:
            answer = 'Yes'
            return

        if l < n and cards1[l] == goal[t]:
            dfs(l + 1, r, t + 1)

        if r < m and cards2[r] == goal[t]:
            dfs(l, r + 1, t + 1)

    dfs(0, 0, 0)
    return answer
