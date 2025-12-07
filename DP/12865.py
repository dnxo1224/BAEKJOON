import sys
import math

# 입력 받기
# N: 물건 개수, K: 배낭 최대 무게
N, K = map(int, sys.stdin.readline().split())

# 물건 정보 저장 (인덱스 1부터 쓰기 위해 앞에 0,0 더미 데이터 추가)
# stuff[i][0]은 무게(W), stuff[i][1]은 가치(V)
stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, sys.stdin.readline().split())))

# DP 테이블 초기화: (N+1) x (K+1) 크기, 0으로 채움
# dp[i][j] : i번째 물건까지 고려했고, 배낭 용량이 j일 때의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

# ---------------------------------------------------------
# [미션] DP 테이블 채우기
# i: 현재 보고 있는 물건 번호 (1 ~ N)
# j: 현재 배낭의 임시 용량 (1 ~ K)
# ---------------------------------------------------------
for i in range(1, N + 1):
    current_weight = stuff[i][0]
    current_value = stuff[i][1]
    
    for j in range(1, K + 1):
        if current_weight > j: # 지금 넣으려는게 배낭의 무게보다 크면, 안들어가겠지? 그러니까 안 넣는 케이스를 작성
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],current_value + dp[i-1][j-current_weight])
            
        

# 정답 출력
print(dp[N][K])