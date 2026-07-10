# Programmers - Level 3. 아방가르드 타일링

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/181186# 'Level 3. 아방가르드 타일링')

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(4, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + prefix[i - 4] * 2 + triple[i - 6] * 2) % MOD
    prefix[i] = (prefix[i - 1] + dp[i]) % MOD
    triple[i] = (triple[i - 3] + dp[i]) % MOD

```

### 설계

- 경우의 수를 저장하는 dp 배열 생성
  - 길이가 4이상일때부터 새로운 패턴은 `2, 2, 4, 2, 2, 4, ...`의 개수로 반복됨
  - 시간복잡도를 줄이기 위해 모든 항에 대한 누적합을 계산한 prefix 배열을 생성하고 점화식에 사용
    - 길이가 `3` 단위로 `2`만큼 더 더해줘야하기 때문에 3의 배수 길이의 누적합을 계산한 triple 배열을 생성하고 점화식에 사용
  - 점화식으로 계산한 경우의 수에 MOD로 나눈 나머지를 저장하고, 각각의 누적합 또한 갱신
