# BAEKJOON ONLINE JUDGE - 15486. 퇴사 2

- [문제출처](https://www.acmicpc.net/problem/15486 "15486. 퇴사 2")

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
result[i]=max(result[i-1],result[i])
if i+t<=n:
    result[i+t-1]=max(result[i+t-1],result[i-1]+p)
```

### 설계

- `i`번째 날의 최대로 받을 수 있는 금액을 저장하면서 진행
    - `i-1`번째 날에 최대로 받을 수 있는 금액과 비교하면서 진행
    - `i`번째 날에 상담을 하면 상담 기간(`t`) 마지막 날(`i+t-1`)의 최대 금액과 비교하여 최댓값 갱신