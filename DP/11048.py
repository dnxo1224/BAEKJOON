# https://www.acmicpc.net/problem/11048
# 이동하기
# 미로 (N,M) 이동하는데 자기 미로에 들어간 숫자가 가장 크도록 밟아야 함. 이동은 우, 하, 대각선(3)

import sys
# input
N ,M= map(int, sys.stdin.readline().split()) 
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#dp 선언
dp = [[0] * (M) for _ in range(N)]

# 초기값 설정
for M in range(M):
    dp[0][M] = A[0][M] + dp[0][M-1]
for N in range(N):
    dp[N][0] = A[N][0] + dp[N-1][0]

# 진행
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = A[i][j] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

print(dp[N][M])