# Programmers - Level 2. 리프 노드 수 최대화

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/468372 'Level 2. 리프 노드 수 최대화')

## 알고리즘 분류

- DFS

## 풀이

### 접근

- `DFS`

### 설계

- 현재 사용할 수 있는 분배 노드에서 자식 노드를 2개 또는 3개를 만드는 경우를 DFS로 탐색
  - 최대한 많은 분배 노드를 다음 depth로 넘길 수 있도록 설정
  - 현재 사용할 수 있는 분배 노드와 분배도가 같으면서 사용한 분배 노드의 개수가 다를 수 있으므로 `visited` dict를 만들어 같은 조건에서 사용한 분배 노드의 수가 작은 경우를 탐색
