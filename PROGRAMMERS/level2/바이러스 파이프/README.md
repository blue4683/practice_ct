# Programmers - Level 2. 바이러스 파이프

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/468373 'Level 2. 바이러스 파이프')

## 풀이

### 접근

- `DFS + BFS`

### 설계

- 주어진 파이프 정보로 그래프 생성
- 감염된 배양체와 이전에 열고 닫은 파이프의 종류를 파라미터로 DFS 수행
  - 이전에 열고 닫은 파이프와 다른 파이프를 대상으로 BFS를 수행해 새로 감염된 배양체를 확인하고 이를 `state`에 반영해서 다음 함수로 넘김
  - `depth`가 `k`와 같아질 때 `state`의 길이와 결과값을 비교해 최댓값을 반영
