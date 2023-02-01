def cal(a,op,b):
    if op=='+':
        return int(a)+int(b)
    elif op == '-':
        return int(a)-int(b)
    elif op == '*':
        return int(a)*int(b)

def dfs(focus, value):
    global high

    if focus == n-1:
        high = max(high, int(value))
        return

    dfs(focus+2, cal(value, me[focus+1], me[focus+2]))
    
    if focus+4<n:
        dfs(focus+4, cal(value, me[focus+1], cal(me[focus+2], me[focus+3], me[focus+4])))

n = int(input())
me = list(input())
high=-1e9
dfs(0,me[0])
print(high)