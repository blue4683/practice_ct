# Programmers - Level 2. [1차] 캐시

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/17680 'Level 2. [1차] 캐시')

## 풀이

### 접근

- `구현`

### 설계

- 도시 이름을 `lower()`로 소문자 변환해 대소문자 구분 없이 비교
- 캐시 히트 시 `+1`, 캐시 미스 시 `+5`로 비용 누적
- LRU 정책을 리스트로 구현
  - 히트 시 `cache.pop(cache.index(city))` 후 다시 `append`해서 맨 뒤(최근 사용)로 이동
  - 미스 시 캐시가 꽉 찼으면 `cache.pop(0)`으로 가장 오래된 항목 제거 후 추가
- `cacheSize`가 `0`인 경우 캐시를 아예 사용하지 않도록 분기 처리
