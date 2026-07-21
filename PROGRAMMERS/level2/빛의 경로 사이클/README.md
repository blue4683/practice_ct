# Programmers - Level 2. 빛의 경로 사이클

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/86052 'Level 2. 빛의 경로 사이클')

## 풀이

### 접근

- `구현`

### 설계

- `y, x, direction`을 인덱스로하는 visited 배열 생성
- 모든 위치 모든 방향을 시작으로 탐색했을 때 지나온 위치와 방향을 다시 방문할 때 사이클 탐색
  - 지나온 곳은 `1`로 사이클인 곳은 `2`로 표현
