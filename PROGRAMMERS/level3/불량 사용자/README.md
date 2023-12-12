# Programmers - Level 3. 불량 사용자

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/64064 'Level 3. 불량 사용자')

## 알고리즘 분류

- 해시

## 풀이

### 설계

- `Set` 활용
- 각 `banned_id` 마다 가능한 `user_id`의 경우들을 찾는다.
- 가능한 경우가 적은 순으로 정렬하여 경우의 수를 찾는다.
  - 조건에 만족하는 경우를 찾으면 정렬 후 `tuple`로 변환하여 `Set`에 저장함으로써 중복을 제거한다.
