from collections import deque

for testcase in range(1,int(input())+1):
    # 접수창구 개수, 정비창구 개수, 손님 수, 찾는 접수창구 번호, 찾는 정비창구 번호
    n,m,k,a,b=map(int,input().split())
    # 접수창구 처리 시간 리스트
    a_time=list(map(int,input().split()))
    # 정비창구 처리 시간 리스트
    b_time=list(map(int,input().split()))
    # 손님 도착 시간 리스트
    t=deque(list(map(int,input().split())))
    # 현재 시간
    time=0
    # 손님 번호
    idx=1
    # 접수창구
    acception=[0]*n
    # 정비창구
    garage=[0]*m
    # 접수를 기다리는 손님 큐
    customers=deque([])
    # 정비를 기다리는 손님 큐
    waiting=deque([])
    # 접수, 정비를 마친 손님의 [손님번호, 접수창구 번호, 정비창구 번호]를 저장하는 리스트
    complete=[]
    # 결과값
    result=0
    while 1:
        # 손님이 도착하는 시간 리스트에 값이 존재하지 않으면 반복문 종료
        while t:
            # 도착하는 시간이 현재 시간과 같다면 도착하는 시간을 꺼내고 손님 큐에 손님 번호 저장
            if t[0]==time:
                t.popleft()
                customers.append([idx])
                idx+=1
            # 다르다면 아직 도착한 손님이 없으므로 반복문 종료
            else:
                break
        # 접수창구 확인
        for i in range(n):
            # 접수창구가 비어있다면 넘어가고
            if not acception[i]: continue
            # 있다면 처리시간 -1
            acception[i][0]-=1
            # 처리가 완료되었다면 [손님 번호, 접수창구 번호]를 waiting(정비를 기다리는 손님)에 저장하고 접수창구 비우기
            if not acception[i][0]:
                waiting.append([acception[i][-1],i+1])
                acception[i]=0
        # 접수할 손님이 없을때까지
        while customers:
            for i in range(n):
                # 접수창구가 비어있다면
                if not acception[i]:
                    # customers 큐의 맨 앞의 손님 번호를 가져와 접수창구에 [접수 처리 시간, 손님 번호]로 저장
                    try:
                        acception[i]=[a_time[i]]+customers.popleft()
                    # customers에 사람이 없다면 반복문 종료
                    except:
                        break
            break
        # 정비창구 확인
        for i in range(m):
            # 정비창구가 비어있다면 넘어가고
            if not garage[i]: continue
            # 있다면 처리시간 -1
            garage[i][0]-=1
            # 처리가 완료되었다면 [손님 번호, 접수창구 번호, 정비창구 번호]를 complete(접수, 정비를 완료한 손님)리스트에 저장하고 정비창구 비우기
            if not garage[i][0]:
                complete.append(garage[i][1:]+[i+1])
                garage[i]=0
        # 정비를 기다리는 손님이 없을때까지
        while waiting:
            for i in range(m):
                # 정비창구가 비어있다면
                if not garage[i]:
                    # waiting 큐의 맨 앞 리스트를 가져와 정비 창구에 [정비 처리 시간, 손님 번호, 접수창구 번호]로 저장
                    try:
                        garage[i]=[b_time[i]]+waiting.popleft()
                    # waiting에 사람이 없다면 반복문 종료
                    except:
                        break
            break
        # 현재 시간 +1
        time+=1
        # 도착한 사람이 없고, 접수 및 정비를 기다리는 사람도 없고, 접수 및 정비창구가 비어있다면 모두 처리했으므로 전체 프로세스 종료
        if not t and not customers and not waiting and acception==[0]*n and garage==[0]*m:
            break
    # 찾는 접수창구 번호와 정비창구 번호가 같다면 결과에 손님 번호 더하기
    for c_num,a_num,b_num in complete:
        if a_num==a and b_num==b:
            result+=c_num
    # 결과값이 0이라면 찾는 손님이 없으므로 -1로 교체
    if not result:
        result=-1
    print(f'#{testcase} {result}')