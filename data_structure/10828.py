import sys

N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    input = list(sys.stdin.readline().strip().split())
    if input[0] == 'push':
        stack.append(int(input[1]))
    elif input[0] == 'pop':
        print((lambda x: x.pop() if x else -1)(stack))
    elif input[0] == 'size':
        print(len(stack))
    elif input[0] == 'empty':
        print(int(not stack))
    elif input[0] == 'top':
        print((lambda x: x[-1] if stack else -1)(stack))
        