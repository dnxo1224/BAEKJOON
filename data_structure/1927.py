'''최소 힙 - heap의 삽입, 삭제 시간 복잡도는 O(log N)'''

import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    input = int(sys.stdin.readline().strip())
    if input == 0: # 최소값 출력하고 그 값 제거
        if len(arr) == 0: # 안에 든게 없을때
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, input)
    