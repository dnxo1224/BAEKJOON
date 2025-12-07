# https://www.acmicpc.net/problem/11055
# 가장 큰 증가하는 부분 수열
# 11053 가장 긴 증가하는 부분 수열의 응용 바리에이션. dp에 값을 먼저 넣어놓은 상태로 증가하는 부분 수열을 찾으면 끝
import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = A[:]

# i : 가장 큰 증가 수열의 마지막 인덱스
# j : 가장 큰 증가 수열을 살펴보는 인자.
for i in range(1,N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max((A[i] + dp[j]), dp[i])

print(max(dp))