# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 3가지 정해진 연산 (3 나누기, 2 나누기, 1 빼기) 를 사용해서 1까지 만드는 횟수의 연산 최솟값 : dp

import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)

# dp[1]은 0이므로 초기화 생략 가능하거나 dp = [0] * (N+1)로 충분

for i in range(2, N + 1):
    # 1. 일단 1을 빼는 경우를 기본값으로 설정
    dp[i] = dp[i-1] + 1
    
    # 2. 2로 나누어 떨어지면? (1을 뺀 것 vs 2로 나눈 것 비교)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        
    # 3. 3으로 나누어 떨어지면? (현재 최솟값 vs 3으로 나눈 것 비교)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
