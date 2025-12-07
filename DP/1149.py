# https://www.acmicpc.net/problem/1149 
# RGB 거리
# R/G/B 세가지 색깔이 서로 반복되지 않도록 배치하는 경우.

import sys
import math
#입력 부분 (가정)
N = int(sys.stdin.readline()) # 집의 수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 빨강 초록 파랑 순으로, 집을 칠할 때 드는 비용.

dp = [[0]*3 for _ in range(N)] # dp 리스트 선언.

# DP 테이블 초기화 (0번째 집은 비용 그대로 시작)
dp[0] = cost[0] # 0번째 집까지 칠할 때 드는 최소 비용은 곧이 곧대로.

for i in range(1,N): # 1번째 집 부터 칠할건데, 칠 할때 드는 최소 비용.
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2]) # 이전에 파랑 초록을 칠했을 때의 최소 비용 + 지금 빨강색을 칠한 비용
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2]) 
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

#정답 출력
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))