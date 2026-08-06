# Programmers - Level 3. [PCCP 기출문제] / 4번 수레 움직이기

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/250134 "Level 3. [PCCP 기출문제] / 4번 수레 움직이기")

## 알고리즘 분류

- DFS

## 풀이

### 접근

- `DFS`

### 설계

- 두 구슬이 이동할 수 있는 경우를 DFS로 탐색
  - 두 구슬이 서로 자리를 바꾸는 경우를 조심히 제외 (AND 연산, OR 사용시 두 구슬이 붙어있을 때 같은 방향으로 한칸씩 움직이는 것도 예외처리에 걸림)