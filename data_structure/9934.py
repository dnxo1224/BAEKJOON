'''완전 이진 트리 - 중위 순회 기반''' 
import sys

K = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().split())) # 상근이가 들어간 건물의 순서 

trees = [[] for _ in range(K)] # 층 별 리스트

def binary_tree(arr, height): # 중위 순회니까 순서 중앙값이 0번째 높이 -> 중앙을 기준으로 왼쪽 값끼리 순서 중앙값 찾고, 오른쪽 값끼리 순서 중앙값 찾아서 대상 값이 1일때까지
    mid_idx = len(arr)//2 # 중간 인덱스 찾기
    trees[height].append(arr[mid_idx]) # 중간 인덱스 넣기
    if len(arr) == 1:
        return
    binary_tree(arr[:mid_idx], height+1) # 왼쪽 먼저 재귀함수
    binary_tree(arr[mid_idx+1:], height+1) # 오른쪽 두번째로 재귀함수

binary_tree(list, 0)
for tree in trees:
    print(*tree) # unpacking - 부수적인거 다 제외하고 값만 출력 '()', '[]' , ',' 등등 제외
    