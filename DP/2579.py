# https://www.acmicpc.net/problem/2579
# 계단오르기. 
# 계단을 오르는데 연속된 세 개의 계단은 밟을 수 없고, 한칸 또는 두칸 이동할 수 있으며 마지막 계단은 무조건 밟아야 함.

import sys

N = int(sys.stdin.readline())

blocks = [int(sys.stdin.readline()) for _ in range(1,N+1)] 

dp = [0]*(301) # N의 최대값

if N<3:
    print(sum(blocks))
else:
    dp[1] = blocks[0]
    dp[2] = blocks[1]+blocks[0]
    for i in range(3,N+1):
        dp[i] = max(dp[i-3]+ blocks[i-1] + blocks[i-2], dp[i-2] + blocks[i-1])
        # 마지막 계단 i를 밟는 경우의 수로 생각을 해야 함.
        # 1. i-3 -> i-1 -> i / 2. i-2 -> i 두가지 경우의 수에 대해 가장 높은 값을 테이블에 집어 넣으면 되는것!
    print(dp[N])