import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp_up = [0 for _ in range(N+1)]
dp_down = [0 for _ in range(N+1)]

dp_up[1] = 1
dp_down[1] = 1

for i in range(2,N+1):
    if A[i-1]>A[i-2]:
        dp_up[i] = dp_up[i-1] + 1
        dp_down[i] = 1
    elif A[i-1]<A[i-2]:
        dp_up[i] = 1
        dp_down[i] = dp_down[i-1] + 1
    elif A[i-1]==A[i-2]:
        dp_up[i] = dp_up[i-1] + 1
        dp_down[i] = dp_down[i-1] + 1

print(max(max(dp_down), max(dp_up)))