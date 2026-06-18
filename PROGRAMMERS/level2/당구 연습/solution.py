def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        left = 10 ** 9 if startY == y and startX > x else (startX + x) ** 2 + (startY - y) ** 2
        right = 10 ** 9 if startY == y and startX < x else (2 * m - startX - x) ** 2 + (startY - y) ** 2
        bottom = 10 ** 9 if startX == x and startY > y else (startX - x) ** 2 + (startY + y) ** 2
        top = 10 ** 9 if startX == x and startY < y else (startX - x) ** 2 + (2 * n - startY - y) ** 2
        answer.append(min(left, right, bottom, top))
        
    return answer
