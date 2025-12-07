# https://www.acmicpc.net/problem/2839
# 설탕 배달
# 동전 최소 갯수 맞추는 문제와 동일한 문제. 3kg과 5kg 으로 N킬로그램을 정확히 맞췄을 때의 최소 봉지 개수

import sys

N = int(sys.stdin.readline())

dp = [5001]*(5005) #최소니까 문제에서 주는 최대 보다 큰 수 넣음.

dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-5]+1,dp[i-3]+1)

if dp[N] > 5000: # dp에 연산이 안된 값들만 -1로 출력
    print(-1)
else:
    print(dp[N])