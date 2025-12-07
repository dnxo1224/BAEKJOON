import sys
N,M = map(int, sys.stdin.readline().split()) # N = 주차 공간의 수 / M = 차랑의 수
Rs = [] # 주차 공간 s의 단위 무게당 요금
Wk = [] # 차량 k의 무게

for _ in range(N):
    Rs.append(int(sys.stdin.readline().strip()))
for _ in range(M):
    Wk.append(int(sys.stdin.readline().strip()))
money = 0 # 주차료 = 무게 X 공간별 가격
park_area = [0] * N # 주차 공간 큐
wait = []
for _ in range(2*M):
    car = (int(sys.stdin.readline().strip()))
    if car > 0: # 들어온다.
        if 0 in park_area: # 빈 공간이 존재한다면
            for i in range(N):
                if park_area[i] == 0: # 빈 공간 위치 파악
                    park_area[i] = car # 차 넣기
                    break
        else: # 공간이 없다.
            wait.append(car)
    else: # 나간다
        idx = park_area.index(-car) # 나가려는 차가 어디 주차되어있는지 확인
        park_area[idx] = 0
        money += Rs[idx]*Wk[-car-1]
        if wait:
            park_area[idx] = wait.pop(0)
print(money)