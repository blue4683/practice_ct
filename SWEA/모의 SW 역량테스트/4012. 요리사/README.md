# SW Expert Academy - 4012. 요리사

* [문제출처](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH "[모의 SW 역량테스트] 요리사")

## 풀이
### 설계
- DFS로 접근
- `n`의 절반동안 재귀 수행
- 재귀 수행 시간을 줄이기 위해 반복문을 바로 직전에 선택한 음식 번호부터 탐색하도록 설정
- `depth`가 `n//2`와 같아지면 선택한 음식과 선택하지 않은 음식으로 나누어서 `A`와 `B`의 음식 맛을 계산
- 최솟값을 `taste`에 저장하고 재귀 종료