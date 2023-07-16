import sys
sys.setrecursionlimit(int(1e9))

def change(depth,word):
    global result
    if result: return
    if depth<=sl:
        result=max(result,int(word==s))
        return result
    if word[-1]=='B': change(depth-1,word[:-1][::-1])
    else: change(depth-1,word[:-1])

s,t=input(),input()
sl,tl=map(len,[s,t])
result=0
if s==t: print(1)
elif tl<=sl: print(0)
else:
    change(tl,t)
    print(result)