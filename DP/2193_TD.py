# https://www.acmicpc.net/problem/2193
# 이친수
# 이친수 : 2진수에서 1이 연속으로 나오지 않는 수

import sys

# 1. 재귀 깊이 제한 설정
sys.setrecursionlimit(10**6)

# 2. 입력 받기
N = int(sys.stdin.readline())

# 3. 메모이제이션 테이블 초기화
# 아직 계산하지 않은 상태는 0으로 표시
dp = [0] * (N + 1)

def solve(n):
    # Base Case (기저 사례)
    # N=1일 때: "1" (1개)
    if n == 1:
        return 1
    # N=2일 때: "10" (1개) -> 11은 안되니까
    if n == 2:
        return 1
    
    # Memoization (이미 계산된 값이면 반환)
    if dp[n] != 0:
        return dp[n]
    
    # ---------------------------------------------------------
    # [미션] 점화식 구현하기 (재귀 호출)
    # 위에서 설명한 논리(끝이 0인 경우 + 끝이 1인 경우)를 코드로 옮기세요.
    # dp[n] = ...
    # ---------------------------------------------------------
    dp[n] = solve(n-1) + solve(n-2)
    
    return dp[n]

# 정답 출력
print(solve(N))