# https://www.acmicpc.net/problem/11726
# 2xn 타일링
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] = dp[i]%10007

print(dp[n]%10007)