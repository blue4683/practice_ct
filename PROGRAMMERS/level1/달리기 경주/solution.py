def solution(players, callings):
    answer = []
    index = {players[i]: i for i in range(len(players))}
    for name in callings:
        i = index[name]
        player = players[i - 1]
        players[i], players[i - 1] = players[i - 1], players[i]
        index[name], index[player] = i - 1, i

    answer = players
    return answer
