# SKOJ - push·pop 연산 복원

- [문제출처](https://skoj.site/problem/10035 'push·pop 연산 복원')

## 풀이

### 접근

- `스택`

### 설계

- `arr`을 `n`부터 `1`까지 역순으로 채워 pop할 때마다 `1, 2, ..., n` 순으로 나오는 push 후보군으로 사용
- 목표값이 `stack` top과 같으면 바로 pop, 다르면 `arr`에서 목표값까지 오름차순으로 전부 push한 뒤 pop
  - `arr` top이 목표값보다 크면 이미 지나쳐서 만들 수 없는 경우이므로 `NO` 처리
