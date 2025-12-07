import sys

def solve():
    """
    백준 15500번 이상한 하노이 탑 문제 풀이 함수
    """
    # 입력을 빠르게 받기 위한 설정
    input_ = sys.stdin.readline

    # 원판의 개수 N 입력
    N = int(input_())

    # 각 기둥을 스택(리스트)으로 표현. 0, 1, 2번 인덱스가 각각 1, 2, 3번 기둥에 해당.
    pegs = [[], [], []]

    # 각 원판이 몇 번 기둥에 있는지 저장하는 리스트 (0번 인덱스는 사용 안 함)
    # 예: disk_location[3] = 0 이면 3번 원판은 1번(0번 인덱스) 기둥에 있다는 의미.
    disk_location = [0] * (N + 1)

    # 초기 상태 입력 (1번 기둥)
    # 입력이 주어지면 리스트로 만들고, 없다면 빈 리스트로 초기화
    try:
        initial_disks = list(map(int, input().split()))
        pegs[0] = initial_disks
        for disk in initial_disks:
            disk_location[disk] = 0
    except (ValueError, IndexError):
        # 입력 줄이 비어있거나 없는 경우를 처리
        pass

    # 이동 횟수와 과정을 저장할 리스트
    moves = []

    # hanoi 함수: from_peg에서 to_peg으로 원판을 옮기는 과정을 기록
    def move_disk(disk, from_peg, to_peg):
        # 이동 과정 기록 (기둥 번호는 1, 2, 3으로 출력해야 하므로 +1)
        moves.append(f"{from_peg + 1} {to_peg + 1}")
        
        # 실제 데이터 구조 변경
        pegs[from_peg].pop()
        pegs[to_peg].append(disk)
        
        # 원판 위치 정보 업데이트
        disk_location[disk] = to_peg

    # 가장 큰 원판(N)부터 1번 원판까지 차례대로 3번 기둥으로 옮긴다.
    for target_disk in range(N, 0, -1): # 3,2,1
        # 목표 원판이 현재 있는 기둥의 번호
        current_peg = disk_location[target_disk]
        
        # 목표 원판이 이미 3번 기둥(인덱스 2)에 있다면 건너뛴다.
        if current_peg == 2:
            continue

        # 방해물을 옮겨 놓을 다른 기둥 찾기
        # current_peg와 목적지(2)가 아닌 나머지 기둥
        # 세 기둥의 인덱스 합은 0+1+2=3 이므로, 3에서 두 기둥 인덱스를 빼면 나머지 하나가 나옴.
        other_peg = 3 - current_peg - 2
        
        # 목표 원판 위에 쌓인 방해물들을 다른 기둥으로 옮긴다.
        # 스택의 맨 위부터 확인하며 목표 원판이 나올 때까지 pop
        while pegs[current_peg][-1] != target_disk:
            disk_to_move = pegs[current_peg][-1]
            move_disk(disk_to_move, current_peg, other_peg)

        # 이제 목표 원판이 맨 위에 있으므로 3번 기둥으로 옮긴다.
        move_disk(target_disk, current_peg, 2)

    # 결과 출력
    print(len(moves))
    # join을 사용해 모든 이동 과정을 한 번에 출력
    print('\n'.join(moves))

# 함수 실행
solve()