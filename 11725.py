import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # 서로 연결됨

visited = [0]* (N+1)

def dfs(node):
    for i in graph[node]: # graph[1] = [6,4]
        if visited[i] == 0:
            visited[i] = node # 6번 4번을 1이 방문했다. visited = [0,0,0,0,1,0,1,0]
            dfs(i) # dif(6), dfs(4) ->  6번은 3번하고 연결, 4번은 2번 7번하고 연결 -> visited = [0,0,4,6,1,0,1,4]

dfs(1)
for i in range(2, N+1):
    print(visited[i])
