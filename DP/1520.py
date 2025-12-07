# https://www.acmicpc.net/problem/1520
# 내리막 길
# 길을 상하좌우 다 갈 수 있지만 조건은 항상 높이가 낮은 곳으로 이동해야 한다는 점. 갈 수 있는 방법의 가짓수 출력

import sys

sys.setrecursionlimit(10 ** 6) # 재귀 깊이 해제

M, N = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)] # M by N 행령

# 이동을 위한 방향 벡터.
dx = [1,-1,0,0] # 0 상, 1 하, 2 좌, 3 우
dy = [0,0,1,-1]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0 # 가짓수 선언 및 초기화

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and A[x][y] > A[nx][ny]:
            ways += dfs(nx,ny)

    dp[x][y] = ways
    return dp[x][y]
    
print(dfs(0, 0))