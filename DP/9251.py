# https://www.acmicpc.net/problem/9251
# LCS 
# 최장 공통 부분 수열 -> 부분 수열 중 가장 긴 부분 문자열을 출력.

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])