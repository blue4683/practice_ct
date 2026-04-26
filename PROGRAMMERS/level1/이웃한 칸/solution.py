def solution(board, h, w):
    answer = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(board)

    def out_of_range(y, x):
        if y < 0 or y >= n or x < 0 or x >= n:
            return 1

        return 0

    for dh, dw in d:
        hh, ww = h + dh, w + dw
        if out_of_range(hh, ww) or board[hh][ww] != board[h][w]:
            continue

        answer += 1

    return answer
