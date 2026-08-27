# Programmers - Level 2. N-Queen

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/12952 'Level 2. N-Queen')

## 풀이

### 접근

- `DFS`

### 설계

- 각 행(`depth`)마다 열(`x`)을 순회하며 기존 배치(`pos`)와 충돌 여부 확인
  - 같은 열이거나 대각선(`abs(xx - x) == abs(yy - depth)`)이면 `break`로 해당 열 제외
- `for-else` 구문으로 끝까지 충돌 없을 때만 `pos`에 좌표 추가하고 다음 행으로 재귀
- 재귀에서 돌아오면 `pos.pop()`으로 백트래킹, `depth == n`이면 `answer` 증가
