# Programmers - Level 2. 과제 진행하기

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/176962 'Level 2. 과제 진행하기')

## 풀이

### 접근

- `스택`

### 설계

- 시작 시간이 빠른 순서대로 stack에 집어넣고 다음으로 시작하는 시간까지 끝낼 수 있는지 stack에 최근에 들어간 과목과 비교해 판단
  - 다음으로 시작하는 시간과 현재 시간의 차이가 stack에 최근에 들어간 과목의 소요 시간보다 크다면 시간 차이에 소요 시간을 뺀 후 stack에서 꺼냄
  - 그렇지 않다면 소요 시간에 시간 차이를 빼주고 stack에 다음 과목을 넣어줌
- plans에 있는 모든 과목을 stack에 넣은 후에도 stack에 과목들이 남아있다면 pop을 통해 꺼내줌
