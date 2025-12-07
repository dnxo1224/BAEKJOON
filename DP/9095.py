# https://www.acmicpc.net/problem/9095
# 1,2,3 더하기
# N을 1,2,3의 덧셈으로 분해하는 연산의 갯수를 구하라.

import sys

T = int(sys.stdin.readline())

testcase = [int(sys.stdin.readline().strip()) for _ in range(T)]

dp = [0]*12

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    print(dp[testcase[i]])
    