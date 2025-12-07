# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수
# 길이에 N인 수에 대해 계단 수의 갯수를 출력하자. (계단수 -> 이웃하는 숫자들이 1차이가 나는 수)

import sys
MOD = 1000000000
N = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(N+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    dp[i][0] = dp[i-1][1]

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    dp[i][9] = dp[i-1][8]

print(sum(dp[N])%MOD)