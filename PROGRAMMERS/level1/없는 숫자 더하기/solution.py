def solution(numbers):
    answer = sum({i for i in range(10)} - set(numbers))
    return answer
