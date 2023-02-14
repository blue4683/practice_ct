def dfs(depth,value):
    '''
    arr[depth]로 접근하여 배열의 끝(depth==n)까지 탐색하면 전역변수인 최소값과 비교 후 함수 종료
    arr[depth]에서 모든 경우의 수를 탐색함
    depth에서 방문한 인덱스는 depth+1이상에서는 방문할 수 없으므로 visited 배열을 통해 탐색 여부 확인
    방문하지 않은 i라면 방문을 체크(visited[i]=1)하고 value에 arr[depth][i]를 더함
    여기서 value가 이미 최소값보다 크다면 원 상태(visited[i]=0 & value-=arr[depth][i])로 돌린 후 더 이상 들어가지 않고 다음 경우의 수를 진행(시간 초과 방지)
    위 경우가 아니라면 다음 행으로 넘어가서 탐색(depth+1)
    depth==n이 되어 탐색이 끝나면 원 상태로 돌린 후 다음 경우의 수를 진행
    :param depth:배열의 깊이
    :param value:누적합
    :return:
    '''
    global min_value
    if depth==n:
        min_value = value if value<min_value else min_value
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            value += arr[depth][i]
            if value>min_value:
                visited[i] = 0
                value -= arr[depth][i]
                continue
            dfs(depth+1,value)
            visited[i]=0
            value -= arr[depth][i]

for testcase in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    min_value = 1e9
    dfs(0,0)
    print(f'#{testcase} {min_value}')