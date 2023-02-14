def rps(a,b):
    '''
    가위바위보 승자를 리스트에 담아 반환하는 함수
    비기는 경우 번호가 더 작은 사람을 승자로 간주
    :param a:번호가 더 작은 사람
    :param b:번호가 더 큰 사람
    :return:
    '''
    if a[-1]-b[-1]==-2:
        return [a]
    elif a[-1]-b[-1]==2:
        return [b]
    elif a[-1]==b[-1]:
        return [a]
    else:
        return [b] if a[-1]<b[-1] else [a]

def tournament(arr):
    '''
    가위바위보 토너먼트 진행하는 재귀함수
    리스트의 길이가 2보다 작다면 부전승으로 리스트 그대로 반환
    리스트의 길이가 2라면 가위바위보 진행 후 승자 반환
    리스트의 길이가 2보다 크면 리스트를 절반으로 나눠서 토너먼트 진행
    리스트의 길이가 짝수일때와 홀수일때 절반으로 나누는 방법이 달라짐
    :param arr: 선수 리스트 [[번호, 가위바위보 카드], [...], ...]
    :return:
    '''
    length = len(arr)
    if length<2:
        return arr
    if length==2:
        return rps(*arr)
    return tournament(arr[:len(arr)//2])+tournament(arr[len(arr)//2:]) if not length%2 else tournament(arr[:len(arr)//2+1])+tournament(arr[len(arr)//2+1:])

for testcase in range(1,int(input())+1):
    n = int(input())
    players = list(map(int,input().split()))
    # 선수들의 번호를 넣어주기 위한 반복문 [[번호, 가위바위보 카드], [...], ...] 형태로 변환
    for idx in range(n):
        players[idx]=[idx+1,players[idx]]
    # 승자가 결정될 때까지 토너먼트 진행
    while len(players)!=1:
        players = tournament(players)
    print(f'#{testcase} {players[0][0]}')