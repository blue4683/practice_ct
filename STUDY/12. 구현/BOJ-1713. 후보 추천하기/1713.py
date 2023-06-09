import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
total=list(map(int,input().split()))

frame=[]
recommend={i:0 for i in range(1,101)}

for num in total:
    if len(frame)<n and num not in frame:
        frame.append(num)
        recommend[num]+=1
    else:
        if num in frame:
            recommend[num]+=1
        else:
            # exclude = [frame에서의 위치 인덱스, 추천 받은 횟수]
            exclude=[0,1000]
            for i in range(len(frame)):
                existed=frame[i]
                if recommend[existed]<exclude[1]:
                    exclude=[i,recommend[existed]]
                    
            recommend[frame[exclude[0]]]=0
            recommend[num]+=1
            frame.pop(exclude[0])
            frame.append(num)

print(*sorted(frame))