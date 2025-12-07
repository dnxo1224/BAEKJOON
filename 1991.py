'''트리 순회'''
import sys

N = int(sys.stdin.readline().strip())
tree = {}

for _ in range(N):
    root, left, right = (sys.stdin.readline().strip().split())
    tree[root] = [left, right] # {A: [B,C]}

def preorder(root):
    if root != '.': # 마지막까지 재귀하면 아무것도 안함
        print(root, end='') #띄어쓰기 안되게 root 출력
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end='') # root 출력
        inorder(tree[root][1]) # right

def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end='') # root 출력

preorder('A')
print()
inorder('A')
print()
postorder('A')