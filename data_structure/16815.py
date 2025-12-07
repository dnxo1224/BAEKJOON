import sys

input = sys.stdin.readline().strip()

index = input.index('*')

input = input[:index]

result = input.count('(') - input.count(')')

print(result)