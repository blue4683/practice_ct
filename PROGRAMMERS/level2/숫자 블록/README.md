# Programmers - Level 2. 숫자 블록

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/12923 'Level 2. 숫자 블록')

## 풀이

### 접근

- `수학`

### 설계

- 각 수의 제곱근 이하 약수 `k`를 순회하며 대응 약수 `num // k` 계산
  - `num // k`가 `10,000,000` 이하면 더 큰 약수이므로 우선 채택, 초과하면 `k` 자체를 후보로 사용
- 소수이거나 약수가 없으면 기본값 `1` 유지, `num < 2`인 경우만 `0`으로 별도 처리
