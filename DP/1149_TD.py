# https://www.acmicpc.net/problem/1149 
# RGB 거리
# R/G/B 세가지 색깔이 서로 반복되지 않도록 배치하는 경우.

import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[-1]*3 for _ in range(N)]

def paint(n, color): # N = 집의 개수, color = 0,1,2 -> RGB
    # 1. 재귀를 끝내고 종료하는 지점 세팅
    if n == 0: 
        return cost[0][color]
    
    # 2. 메모이제이션 세팅
    if dp[n][color] != -1: # dp[N][color] 안에 값이 있으면 가져다 와서 쓰기.
        return dp[n][color]
    
    # 3. 점화식 세팅
    if color == 0:
        dp[n][0] = cost[n][0] + min(paint(n-1, 1), paint(n-1, 2))
    elif color == 1:
        dp[n][1] = cost[n][1] + min(paint(n-1, 0), paint(n-1, 2))
    elif color == 2:
        dp[n][2] = cost[n][2] + min(paint(n-1, 1), paint(n-1, 0))
    else:
        return -1
    
    return dp[N][color]
# 출력
print(min(paint(N-1, 0), paint(N-1, 1), paint(N-1, 2)))