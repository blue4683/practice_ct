# BAEKJOON ONLINE JUDGE - 1932. 정수 삼각형

- [문제출처](https://www.acmicpc.net/problem/1932 "1932. 정수 삼각형")

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
if j==0: result[i][j]=result[i-1][j]+triangle[i][j]
elif j==i: result[i][j]=result[i-1][j-1]+triangle[i][j]
else: result[i][j]=max(result[i-1][j-1],result[i-1][j])+triangle[i][j]
```

### 설계

- 점화식 구현
    - 자식 노드가 부모 노드 두개 중 하나를 선택했을 때 가질 수 있는 최대 합 저장
    - 가장 왼쪽과 오른쪽 자식 노드는 하나의 부모만 선택할 수 있으므로 예외처리