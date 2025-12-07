import sys

# 1. 테스트 케이스 개수 입력 (변수명을 T로 변경하여 헷갈림 방지)
T = int(sys.stdin.readline())

# 2. DP 테이블 초기화 (수정됨)
# 입력되는 N은 최대 40이므로, 인덱스 40까지 접근하려면 크기가 41이어야 함
# 테스트 케이스 개수(T)와 상관없이 고정된 크기입니다.
dp = [[0, 0] for _ in range(41)]

# 3. 초기값 설정 (Base Case)
dp[0] = [1, 0]
dp[1] = [0, 1]

# 4. 점화식으로 테이블 미리 채우기 (Pre-computation)
# 0과 1은 채웠으니 2부터 40까지 채움
for i in range(2, 41):
    # 0이 출력되는 횟수 = (i-1)의 0횟수 + (i-2)의 0횟수
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    # 1이 출력되는 횟수 = (i-1)의 1횟수 + (i-2)의 1횟수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

# 5. 정답 출력
for _ in range(T):
    # 각 테스트 케이스마다 N을 입력받고, 미리 구해둔 dp[N] 출력
    N = int(sys.stdin.readline())
    print(dp[N][0], dp[N][1])