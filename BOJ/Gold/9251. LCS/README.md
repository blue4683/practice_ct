# BAEKJOON ONLINE JUDGE - 9251. LCS

- [문제출처](https://www.acmicpc.net/problem/9251 "9251. LCS")

## 알고리즘 분류

- 다이나믹 프로그래밍
- 문자열

## 풀이

### 접근

- `DP`

### 점화식

```python
if i==0 or j==0: lcs[i][j]=0
elif a[i-1]==b[j-1]: lcs[i][j]=lcs[i-1][j-1]+1
else: lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
```

### 설계

- 두 문자열을 한 글자씩 비교한다.
- 두 문자가 다르면 `lcs[i][j-1]`과 `lcs[i-1][j]` 중에 큰 값을 저장한다.
- 두 문자가 같으면 `lcs[i-1][j-1]` 값에 1을 더해 저장한다.
- 위 과정을 반복한다.