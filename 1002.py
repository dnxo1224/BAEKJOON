import math

rep = input()
for i in range(int(rep)):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    length = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

    if (x1==x2 and y1==y2 and r1 != r2):
        result = 0
    elif(x1==x2 and y1==y2 and r1 == r2):
        result = -1
    elif ((length == (r1+r2)) or (length == abs(r1-r2))):
        result = 1
    elif ((length > (r1+r2)) or (length < abs(r1-r2))):
        result = 0
    else:
        result = 2
    print(result)