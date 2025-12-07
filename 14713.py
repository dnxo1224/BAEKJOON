'''앵무새'''
import sys
S = []
N = int(sys.stdin.readline().strip())

for _ in range(N):
    S.append(sys.stdin.readline().split())

L = list(sys.stdin.readline().split())

while L:
    flag = False
    for i in range(N):
        if S[i]:
            if L[0] == S[i][0]:
                L.pop(0)
                S[i].pop(0)
                flag = True
                break
    if not flag:
        print("Impossible")
        break
else:
    if any(S): # S안에 하나라도 참이 있으면 True , [] [] []는 False
        print("Impossible")
    else:
        print("Possible")
