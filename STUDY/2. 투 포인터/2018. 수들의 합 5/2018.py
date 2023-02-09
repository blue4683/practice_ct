n=int(input())
cnt=1
start=1
end=1
sum_value=1
while end!=n:
    if sum_value==n:
        cnt+=1
        end+=1
        sum_value+=end
    elif sum_value>n:
        sum_value-=start
        start+=1
    else:
        end+=1
        sum_value+=end  
print(cnt)