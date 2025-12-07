import sys

N = int(sys.stdin.readline())

# 1. 초기값 수정: 충분히 큰 수로 설정
dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    # 2. 로직 수정: elif 대신 각각의 경우를 모두 비교하여 최솟값 갱신
    
    # 1원 동전을 낼 때
    if i >= 1:
        dp[i] = min(dp[i], dp[i-1] + 1)
        
    # 2원 동전을 낼 때
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + 1)
        
    # 5원 동전을 낼 때
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] + 1)
        
    # 7원 동전을 낼 때
    if i >= 7:
        dp[i] = min(dp[i], dp[i-7] + 1)

# 정답 출력
print(dp[N])