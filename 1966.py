t = int(input()) # t 번 입력 받겠다.

for _ in range(t):
    n, m = map(int, input().split()) # n개의 list 입력 list의 m번째 숫자 추적
    data = list(map(int, input().split())) # list
    
    result = 1
    while data: # list에서 
        if data[0] < max(data): #  list 가장 앞에있는 숫자보다 큰 숫자가 리스트에 존재하는가?
            data.append(data.pop(0)) # 그럼 맨 앞 숫자는 list 맨 뒤롤 이동

        else: # 맨 앞에있는게 가장 큰 값일때,
            if m == 0: break # 추적하는 숫자가 맨 앞일 때 while 빠져나와서 결과 출력

            data.pop(0) # 맨 앞에 있는 숫자 빼내기 - 가장 큰 값이 앞에 와있는데 걔가 우리가 추적하는 애가 아님.
            result += 1 # 하나 빼냈으니까 result 1 올리기 

        m = m - 1 if m > 0 else len(data) - 1 # 맨 앞에있는 숫자가 빠지면 m 은 앞으로 이동한다. m 이 0이었으면 맨 뒤로 보낸다.
    print(result)