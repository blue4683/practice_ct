def dfs(depth, result, n, numbers, target):
    global answer
    if depth==n:
        if result == target:
            answer+=1
        return
    dfs(depth+1, result + numbers[depth], n, numbers, target)
    dfs(depth+1, result - numbers[depth], n, numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    dfs(0, 0, n, numbers, target)
    return answer
