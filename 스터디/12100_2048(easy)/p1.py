from itertools import product
from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_number = 0


# 블록 이동
def game(arr, line, reverse=False):
    global max_number
    new_line = []
    last = 0
    for j in range(n):
        if line[j]:
            # 블록 합치기
            if line[j] == last:
                max_number = max(max_number, last * 2)
                new_line[-1] *= 2
                last = 0    # 이미 합쳐진 블록은 다시 합치지 않도록 변수 초기화
            # 단순 이동
            else:
                last = line[j]
                max_number = max(max_number, last)
                new_line.append(line[j])

    new_line += [0] * (n - len(new_line))
    if reverse:     # 우, 하 방향의 경우 반대로 합쳐줌
        arr.append(new_line[::-1])
    else:
        arr.append(new_line)


# 중복순열을 사용하여 가능한 경우를 다 알아봄
for case in product(range(1, 5), repeat=5):
    case_board = deepcopy(board)
    for c in case:
        new_board = []
        if c in [1, 2]:      # 1: 상, 2: 하
            for i in zip(*case_board):
                line = i
                if c == 1:
                    game(new_board, line)
                else:
                    game(new_board, line[::-1], True)
            case_board = [i for i in zip(*new_board)]
        else:
            for i in range(n):
                line = case_board[i]
                if c == 3:          # 3: 좌
                    game(new_board, line)
                else:               # 4: 우
                    game(new_board, line[::-1], True)
            case_board = new_board

print(max_number)