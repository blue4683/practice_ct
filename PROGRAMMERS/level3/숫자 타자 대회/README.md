# Programmers - Level 3. 숫자 타자 대회

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/136797 'Level 3. 숫자 타자 대회')

## 풀이

### 접근

- `다익스트라`

### 설계

- 각 자판의 위치에서 다른 자판을 누르기 위한 비용을 `dist`에 저장
- 다익스트라로 주어진 숫자를 칠 수 있는 최소 비용을 탐색
  - 왼손 엄지와 오른손 엄지가 겹치지 않도록 탐색
