def factorial(num):
    if not num:
        return 1
    
    return num * factorial(num - 1)

n = int(input())
print(factorial(n))
