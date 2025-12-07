'''binarytree'''

import sys

n = int(sys.stdin.readline().strip()) # 7

parent = [int(sys.stdin.readline().strip()) for _ in range(n)] # -1 1 1 2 2 3 3

depth = [0 for _ in range(n)] # 0 0 0 0 0 0 0

for i in range(n):
    if parent[i] == -1:
        continue
    depth[i] = depth[parent[i]-1]+1
for i in range(n):
    print(f'{depth[i]}')

# 0 1 1 2 2 2 2
