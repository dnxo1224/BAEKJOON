'''괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. '''

import sys

data_T = int(sys.stdin.readline().strip()) # int 값 받기
data_list = [(sys.stdin.readline().strip()) for _ in range(data_T)] # 데이터 T개 입력받기

for i in range(len(data_list)): # 데이터 T개 만큼 반복
    validation_stack = [] # 괄호 검증을 위한 stack 선언 및 초기화
    for j in data_list[i]: # i번째 데이터 str 하나씩 확인
        if j == '(':
            validation_stack.append(j) # 여는괄호 나오면 스택에 여는 괄호를 저장
        elif j == ')':
            if validation_stack: # 여는괄호가 나온 적 있다 -> 스택에 있는거 pop하고 얘는 통과
                validation_stack.pop()
            else:
                print("NO") # 여는괄호가 나온 적 없고 닫는 괄호만 나왔다.
                break
    else:
        if not validation_stack: # 스택 깔끔
            print("YES") 
        else: # 다 돌렸는데 스택에 빼내지 못한 여는괄호가 존재한다.
            print("NO")