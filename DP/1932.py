import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

dp[0][0] = arr[0][0]

if n < 2:
    print(arr[0][0])
else:
    for i in range(n):
        for j in range(i+1):
            if j < 1:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            else:
                dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    print(max(dp[-1]))