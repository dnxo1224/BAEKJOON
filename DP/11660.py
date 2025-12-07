# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5
# 좌표 A부터 B까지의 2차원 배열의 구간 합을 구하는 문제.

import sys

N,M = map(int, sys.stdin.readline().split())

A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)] # 1번 인덱스 부터 사용할게요.

for i in range(1,N+1):
    for j in range(1, N+1):
        dp[i][j] = A[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] 

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    
    print(result)