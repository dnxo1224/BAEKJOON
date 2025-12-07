# import sys

# stack = []
# slice_ = 0
# result = 0
# batch = sys.stdin.readline().strip()
# batch_re = batch.replace('()','*')

# for i in batch_re:  
#     if i == ')':
#         while stack[-1] != '(':
#             last = stack.pop()
#             if last == '*':
#                 slice_ += 1
#         result += slice_ + 1
#         stack.pop()
#         for _ in range(slice_):
#             stack.append('*')
#         slice_ = 0
#     stack.append(i)

# print(result)

ir= input()
stack=[]
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":  # 레이저 쏘기
            stack.pop()
            cnt+=len(stack) # 현재의 쇠막대기들을 카운팅
            
        else :
            stack.pop()
            cnt+=1 # 이 부분은 두 번째 경우인  (()())  일때 나머지 부분을 세는 것입니다.
print(cnt)