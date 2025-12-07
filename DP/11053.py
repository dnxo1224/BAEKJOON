# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# 주어진 수열에서 증가하는 부분 중 가장 긴 부분의 길이를 출력.

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
