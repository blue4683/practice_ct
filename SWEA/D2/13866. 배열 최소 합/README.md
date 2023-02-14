# SW Expert Academy - 13866. 배열 최소 합

* [문제출처](https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVIc7KqfQDFAWg# "13866. 배열 최소 합")

## 풀이
### 1차 시도
- 백트래킹으로 접근
- arr[depth]로 접근하여 배열의 끝(depth==n)까지 탐색하면 전역변수인 최소값과 비교 후 함수 종료
- arr[depth]에서 모든 경우의 수를 탐색함
- depth에서 방문한 인덱스는 depth+1이상에서는 방문할 수 없으므로 visited 배열을 통해 탐색 여부 확인
- 방문하지 않은 i라면 방문을 체크(visited[i]=1)하고 value에 arr[depth][i]를 더함
- 다음 행으로 넘어가서 탐색(depth+1)
- depth==n이 되어 탐색이 끝나면 원 상태로 돌린 후 다음 경우의 수를 진행
- 시간 초과

### 2차 시도
- arr[depth]에서 경우의 수를 탐색할 때 조건을 주어 시간 초과 방지
- value가 이미 최소값보다 크다면 원 상태(visited[i]=0 & value-=arr[depth][i])로 돌린 후 더 이상 들어가지 않고 다음 경우의 수를 진행