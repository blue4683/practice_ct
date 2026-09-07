# SKOJ - 덱의 회전 최소 횟수

- [문제출처](https://skoj.site/problem/10046 '덱의 회전 최소 횟수')

## 풀이

### 접근

- `구현`

### 설계

- 매 타겟마다 `q.index(target)`로 현재 위치(`idx`) 확인, 이미 맨 앞이면 `popleft`로 바로 제거
- 왼쪽 회전(`idx`번)과 오른쪽 회전(`len(q)-idx`번) 중 적은 쪽을 선택해 `q[0]`이 타겟이 될 때까지 회전 반복, 회전마다 `result` 증가
  - 왼쪽 회전은 `append(popleft())`, 오른쪽 회전은 `appendleft(pop())`로 구현
- 타겟이 맨 앞에 오면 `popleft`로 제거하고 다음 타겟으로 진행