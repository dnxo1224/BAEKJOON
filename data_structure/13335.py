import sys
n,w,L = map(int, (sys.stdin.readline().split()))

queue = list(map(int,sys.stdin.readline().split()))

bridge = [0]*w # if w = 4, [0][0][0][0] 다리에 w개의 공간을 만들어줌
time = 0
while bridge:
    time += 1
    bridge.pop(0) # 젤 앞에꺼 한칸 빼기
    if queue:
        if sum(bridge) + queue[0] <= L:
            bridge.append(queue.pop(0))
        else:
            bridge.append(0)

print(time)
