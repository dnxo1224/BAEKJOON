'''정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque

queue = deque() # 스택처럼 써도되고 큐 처럼 써도 됨.  / 이쪽으로 큐 출력 <- [ [] [] [] [] ] <- 이쪽으로 큐 입력
N = int(sys.stdin.readline()) # N번의 명령어 입력

for _ in range(N) : 
    i = sys.stdin.readline().split() # 명령어 입력

    if i[0] == 'push' : # 큐에 X를 넣기
        queue.append(int(i[1])) 
    
    elif i[0] == 'pop' : # 큐에서 가장 앞에있는거 뺴고 그거 출력, 만약 큐에 아무것도 없으면 -1 출력
        if not queue :
            print (-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif i[0] == 'size' : # len(queue) 하면 됨
        print(len(queue))
    
    elif i[0] == 'empty' : # is queue 이면 1 출력 아니면 0
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' : # queue에 가장 앞에있는거 출력
        if not queue:
            print(-1)
        else :
            print(queue[0])
    
    elif i[0] == 'back' : # queue에 가장 뒤에있는거 출력
        if not queue :
            print(-1)
        else :
            print(queue[-1])