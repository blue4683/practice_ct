def solution(s):
    answer = 0
    stack = []
    for c in s * 2:
        if stack and stack[-1] + c in {'[]', '{}', '()'}:
            stack.pop()
            if not stack or stack[-1] in {']', '}', ')'}:
                answer += 1
            
        else:
            stack.append(c)
            
    stack = []
    for c in s:
        if stack and stack[-1] + c in {'[]', '{}', '()'}:
            stack.pop()
            if not stack or stack[-1] in {']', '}', ')'}:
                answer -= 1
            
        else:
            stack.append(c)
            
    return answer
