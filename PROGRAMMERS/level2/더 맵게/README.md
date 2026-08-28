# Programmers - Level 2. 더 맵게

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/42626 'Level 2. 더 맵게')

## 풀이

### 접근

- `힙`

### 설계

- 스코빌 지수 리스트를 최소 힙(`heapify`)으로 구성
- 최솟값이 `K` 이상이 될 때까지 최솟값 두 개(`x`, `y`)를 꺼내 `x + 2*y` 공식으로 섞은 뒤 다시 삽입, 섞은 횟수를 `answer`에 누적
  - `x`가 이미 `K` 이상이면 다시 push하지 않고 바로 break — 힙 특성상 나머지 원소도 전부 `x` 이상이라 `scoville[0]`도 여전히 `K` 이상이므로 결과에는 영향 없음
- 반복이 끝난 뒤 남은 최솟값이 `K` 미만이면 -1, 아니면 `answer` 반환
