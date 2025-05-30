# BAEKJOON ONLINE JUDGE - 2304. 창고 다각형

- [문제출처](https://www.acmicpc.net/problem/2304 '2304. 창고 다각형')

## 알고리즘 분류

- 자료 구조
- 브루트포스
- 스택

## 풀이

### 접근

- 구현

### 설계

- 이전 기둥의 높이보다 높아질 때마다 스택에 저장
  - `현재 기둥과 이전 기둥의 x 좌표 차이 * 이전 기둥의 높이` 만큼 결과값에 더해줌
  - 왼쪽에서 탐색하는 경우와 오른쪽에서 탐색하는 경우 구현
- 마지막에 왼쪽에서 탐색했을 때 가장 높이가 높은 기둥의 `x` 좌표와 오른쪽에서 탐색했을 때의 `x` 좌표의 차이에 `1`을 더한 값에 높이를 곱해서 결과값에 더해준 뒤 출력
