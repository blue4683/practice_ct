# Programmers - Level 2. 다리를 지나는 트럭

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/42583 'Level 2. 다리를 지나는 트럭')

## 풀이

### 접근

- `큐`

### 설계

- 다리 위의 트럭을 `(다리를 벗어나는 시각, 무게)` 튜플로 큐에 저장해 시간 경과에 따라 통과 처리
- 매 초(`answer`)마다 벗어날 시각이 된 트럭을 큐에서 빼고 `total`에서 무게를 차감
  - 남은 무게(`weight - total`)가 다음 대기 트럭 무게보다 작으면 이번 초는 건너뜀
- 대기 트럭(`q`)과 다리 위 트럭(`bridge`)이 모두 빌 때까지 반복
