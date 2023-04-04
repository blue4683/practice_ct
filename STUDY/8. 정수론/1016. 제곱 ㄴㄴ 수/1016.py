MIN,MAX=map(int,input().split())
arr=[0]*(MAX-MIN+1)
for i in range(2,int(MAX**0.5)+1):
    P=i**2
    start=MIN//P
    if MIN%P: start+=1
    for j in range(start,MAX//P+1):
        arr[j*P-MIN]=1
print(arr.count(0))

# MIN,MAX=map(int,input().split())
# LIMIT=int(1e6)
# result=MAX-MIN+1
# arr=[0]*(LIMIT+1)
# Prime=[]
# for i in range(2,LIMIT+1):
#     if arr[i]: continue
#     if i**2<=int(1e6):
#         Prime+=[i**2]
#     j=2
#     while i*j<=int(1e6):
#         arr[i*j]=1
#         j+=1
# arr=[0]*(MAX-MIN+1)
# arr[0]=1
# for P in Prime:
#     j=0
#     while P*j<=MAX-MIN:
#         if not arr[P*j]:
#             arr[P*j]=1
#             result-=1
#         j+=1
# print(arr.count(0))