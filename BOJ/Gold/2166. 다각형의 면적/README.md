# BAEKJOON ONLINE JUDGE - 2166. 다각형의 면적

- [문제출처](https://www.acmicpc.net/problem/2166 '2166. 다각형의 면적')

## 알고리즘 분류

- 기하학
- 다각형의 넓이

## 풀이

### 설계

- 다각형의 넓이 공식은 다음과 같다.

  $$
      S = \frac{1}{2} \left | \sum_{i=1}^{n} (x_{i} + x_{i+1})(y_{i} - y_{i+1}) \right |
  $$

- `n+1`과 연결된 점은 0번 점이므로 0번 점을 끝에 추가해준다.
