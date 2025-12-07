'''
left 스택과 right 스택을 만들고 그 사이에 커서가 위치하게끔 설계.
'''
import sys
left = list(sys.stdin.readline().strip()) # abcd
right = []
command_num = int(sys.stdin.readline().strip()) # 3

for _ in range(command_num):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

result = left + right[::-1]
print(''.join(result))