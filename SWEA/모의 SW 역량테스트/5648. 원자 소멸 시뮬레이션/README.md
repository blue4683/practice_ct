# SW Expert Academy - 5648. 원자 소멸 시뮬레이션

* [문제출처](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo "[모의 SW 역량테스트] 원자 소멸 시뮬레이션")

## 풀이
### 설계
- 원자가 이동하는 도중 만날 수도 있으므로 0.5초 단위로 구현
- 리스트로 구현할 경우 메모리 오버가 나기 때문에 딕셔너리로 구현
- 딕셔너리에 `좌표:원자 정보`를 저장하고 원자 정보가 2개 이상이라면 원자가 만났으므로 결과값에 두 에너지를 더해준다.
- 원자가 모두 사라질때까지 반복문 진행