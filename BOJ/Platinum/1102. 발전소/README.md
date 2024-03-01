# BAEKJOON ONLINE JUDGE - 1102. 발전소

- [문제출처](https://www.acmicpc.net/problem/1102 '1102. 발전소')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
    if dp[i][next_bit] == -1:
        dp[i][next_bit] = dp[i - 1][bit] + cost

    else:
        dp[i][next_bit] = min(
            dp[i][next_bit], dp[i - 1][bit] + cost)
```

### 설계

- 현재 켜져있는 발전소를 비트필드로 구현
- 켜져있는 발전소로 꺼져있는 발전소를 키는데 드는 최소 비용을 배열에 저장
  - 켜져있는 발전소의 최소 개수만큼 탐색을 진행하고 가장 비용이 적은 경우를 출력
