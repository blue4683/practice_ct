# SW Expert Academy - 4013. 특이한 자석

* [문제출처](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH "[모의 SW 역량테스트] 특이한 자석")

## 풀이
### 설계
- 자석의 회전을 구현할 때 시간을 줄이기 위해서 `deque`을 사용해 자석 구현
- 주어진 번호와 방향을 통해 자석이 회전하는지를 확인하는 함수 구현
- 주어진 번호의 좌우를 확인하여 붙어있는 부분의 극이 다르면 `next`에 넣어 자석을 회전시키고, `q`에 그 옆에있는 자석을 넣어 확인한다.
- 극이 같다면 아무것도 하지 않는다.
- 회전시킬 자석을 찾은뒤 방향에 따라 자석을 회전시킨다.
- 위의 과정을 `k`만큼 진행하고 각 `deque`의 `0`번째 인덱스가 `1`인 경우 결과값에 `2**index`만큼 더해준다.