import sys
import heapq

# 입력 속도 가속
input = sys.stdin.readline

# V: 정점 개수, E: 간선 개수
V, E = map(int, input().split())

# 인접 리스트 생성 (graph[u] = [(가중치, v), ...])
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

# 방문 체크 리스트
visited = [False] * (V + 1)

# 우선순위 큐 (Min Heap) - 시작점 1번 노드, 가중치 0
heap = [[0, 1]]  # (가중치, 노드번호)

total_weight = 0 # MST 가중치 합
cnt = 0 # 연결된 간선 수 (V-1개가 되면 종료해도 됨)

while heap:
    if cnt == V:
        break # 모든 노드 방문 완료 시 조기 종료
    w, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        total_weight += w
        cnt += 1
        for i in graph[node]:
            next_w, next_node = i
            if not visited[next_node]:
                heapq.heappush(heap, [next_w, next_node])

print(total_weight)