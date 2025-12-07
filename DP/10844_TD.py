# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수
# 길이에 N인 수에 대해 계단 수의 갯수를 출력하자. (계단수 -> 이웃하는 숫자들이 1차이가 나는 수)

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
MOD = 1000000000

# 메모이제이션 테이블 (-1로 초기화)
# dp[len][digit]
dp = [[-1] * 10 for _ in range(N + 1)]

def solve(length, digit):
    # 1. 범위를 벗어난 숫자 (0~9 아님) 체크 -> 불가능하므로 0 반환
    if digit < 0 or digit > 9:
        return 0
        
    # 2. 기저 사례: 길이가 1에 도달하면 카운트 1 (유효한 경로 하나 찾음)
    if length == 1:
        return 1
    
    # 3. 메모이제이션: 이미 계산한 값이면 반환
    if dp[length][digit] != -1:
        return dp[length][digit]
    
    # 4. 점화식 (재귀 호출)
    # 내 자리가 digit이려면, 바로 앞자리(length-1)는 digit-1 또는 digit+1이어야 함
    dp[length][digit] = (solve(length - 1, digit - 1) + solve(length - 1, digit + 1)) % MOD
    
    return dp[length][digit]

# 정답 구하기
result = 0
# 시작하는 숫자는 1부터 9까지 가능 (0은 불가능)
# 길이는 N이고, 마지막 숫자가 i인 경우를 모두 더함
# 주의: Top-Down은 보통 '위에서 아래로'지만, 여기선 논리상
# "길이 N의 마지막 자리가 i일 때"를 구하기 위해 재귀를 돕니다.
for i in range(1, 10):
    result = (result + solve(N, i)) % MOD

print(result)