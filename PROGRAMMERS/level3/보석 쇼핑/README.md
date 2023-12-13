# Programmers - Level 3. 보석 쇼핑

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/67258 'Level 3. 보석 쇼핑')

## 알고리즘 분류

- 투 포인터
- 해시

## 풀이

### 설계

- 투 포인터 + `defaultdict` 활용
  - `defaultdict`에 종류별 보석 수를 기록하면서 탐색
  - 모든 보석이 존재하면 저장
  - 투 포인터 탐색이 끝나고 범위가 작은 순으로 정렬 후 맨 처음 값 출력
