# Programmers - Level 2. 연속된 부분 수열의 합

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/178870 'Level 2. 연속된 부분 수열의 합')

## 풀이

### 접근

- `투포인터`

### 설계

- 0에 포인터를 지정하고 합이 작으면 `r`을 합이 크면 `l`을 증가시키고 총합을 갱신하면서 총합이 `k`를 만족하면서 구간의 길이가 가장 작은 구간을 탐색
