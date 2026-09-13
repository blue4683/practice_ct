# SKOJ - 차례대로 다시 줄 서기

- [문제출처](https://skoj.site/problem/10282 '차례대로 다시 줄 서기')

## 풀이

### 접근

- `큐(Deque)`

### 설계

- `1`부터 `N`까지 번호를 `deque`에 담고, `OUT`은 `popleft()`, `MOVE`는 `popleft()` 후 `append()`로 맨 뒤로 보내는 방식으로 시뮬레이션
- 모든 명령 처리 후 큐가 비어 있으면 `EMPTY`, 아니면 남은 사람을 앞에서부터 한 줄에 출력
