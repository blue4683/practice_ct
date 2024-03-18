# BAEKJOON ONLINE JUDGE - 1040. 정수

- [문제출처](https://www.acmicpc.net/problem/1040 '1040. 정수')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
ret = 0

if zero and n[pos] == 0:
    next_val = solve(pos + 1, used, big, zero)
    if next_val >= 0:
        return next_val

for i in range(0 if big else n[pos], 10):
    if zero and i == 0:
        continue

    next_val = solve(pos + 1, used | (1 << i),
                        big or (i > n[pos]), zero and (i == 0))
    if next_val >= 0:
        ret = next_val + ten[pos] * i
        return ret
```

### 설계

- `dp[pos][used][big][zero]`: `pos`번째 자리의 수를 정할 때 사용된 수를 `used` 비트로 저장하고 이전 수보다 크다면 `big == 1`로 저장, `0`을 사용했다면 `zero == 1`로 저장
- 1의 자리부터 숫자를 변경하면서 조건에 맞는지 확인하며 탐색
