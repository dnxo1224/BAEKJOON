# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# 주어진 수열에서 증가하는 부분 중 가장 긴 부분의 길이를 출력.

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]

def solve(i):
    # 2. 메모이제이션
    if dp[i] != 0:
        return dp[i]
    
    # 일단 나 혼자일 때의 길이 1
    max_len = 1

    # 내 앞의 녀석들을 탐색
    for j in range(i):
        if arr[j] < arr[i]:
            max_len = max(max_len, solve(j) + 1)
    
    # 결과 저장 및 반환
    dp[i] = max_len

    return dp[i]

result = 0

for i in range(N):
    result = max(solve(i), result)
print(result)