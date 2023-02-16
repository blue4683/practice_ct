# n=int(input())
# card=[i for i in range(1,n+1)]
# while len(card)>1:
#     tmp=card[1::2]
#     if not len(card)%2:
#         card=tmp
#     else:
#         tmp.append(tmp.pop(0))
#         card=tmp
# print(*card)

n=int(input())
card=[i for i in range(1,n+1)]
while len(card)>1:
    tmp=card[1::2]
    if not n%2:
        card=tmp
    else:
        tmp.append(tmp.pop(0))
        card=tmp
    n//=2
print(*card)