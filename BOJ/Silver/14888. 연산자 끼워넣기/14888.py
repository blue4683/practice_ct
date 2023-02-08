def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a*b < 0:
        return -(abs(a)//b)
    return a//b

def calculate(depth, num):
    global resultMin, resultMax, add, sub, mul, div

    if depth == N:
        resultMin = min(resultMin, num)
        resultMax = max(resultMax, num)

    if add > 0:
        add -= 1
        calculate(depth+1, plus(num,numList[depth]))
        add += 1
    if sub > 0:
        sub -= 1
        calculate(depth+1, minus(num,numList[depth]))
        sub += 1
    if mul > 0:
        mul -= 1
        calculate(depth+1, multiply(num,numList[depth]))
        mul += 1
    if div > 0:
        div -= 1
        calculate(depth+1, divide(num, numList[depth]))
        div += 1
            
N = int(input())
numList = list(map(int,input().split()))
add, sub, mul, div = list(map(int,input().split()))
    
resultMin =  10**9
resultMax = -10**9
calculate(1, numList[0])
print(resultMax)
print(resultMin)