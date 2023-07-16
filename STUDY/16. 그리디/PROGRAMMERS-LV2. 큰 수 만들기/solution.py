def solution(number, k):
    answer = ''
    n=len(number)
    stack=[]
    for num in number:
        while stack and k and int(num)>int(stack[-1]):
            stack.pop()
            k-=1
        stack.append(num)
        
    if k: stack=stack[:-k]
    answer=''.join(stack)
    
    return answer