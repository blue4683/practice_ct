# Programmers - Level 2. 완전범죄

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/389480 'Level 2. 완전범죄')

## 풀이

### 접근

- `DFS`

### 설계

- DFS로 A와 B가 훔치는 경우를 탐색
  - 시간 초과를 방지하기 위해 A의 흔적이 최소 결과값보다 커지는 경우나 이전에 탐색한 경우를 `set`에 저장해 중복 탐색을 방지
