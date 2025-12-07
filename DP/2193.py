# https://www.acmicpc.net/problem/2193
# 이친수
# 0과1로 이루어진 2진수 중에 1이 연속해서 나오지 않는 수를 이친수라 부른다. N자리 이친수의 가짓수를 구하여라.
import sys

N = int(sys.stdin.readline())

dp_0 = [0 for _ in range(N+1)]
dp_1 = [0 for _ in range(N+1)]

dp_1[1] = 1

for i in range(2,N+1):
    dp_0[i] = dp_0[i-1] + dp_1[i-1]
    dp_1[i] = dp_0[i-1]

print(dp_0[-1]+dp_1[-1])
