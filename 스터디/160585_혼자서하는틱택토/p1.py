# 프로그래머스 160585. 혼자서 하는 틱택토

def solution(board):
    first, second, first_list, second_list = count_attack(board)

    # X가 더 많은 경우,
    if second > first:
        return 0

    # O가 2개 이상 더 많은 경우,
    if first - 1 > second:
        return 0

    # X를 완성했는데, O가 더 많음
    if first > second:
        return check_success(second_list)
    # O를 완성했는데, X 개수가 똑같음
    elif first == second:
        return check_success(first_list)


def count_attack(board):
    first = 0
    second = 0
    first_list = []
    second_list = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                first += 1
                first_list.append([i, j])
            elif board[i][j] == 'X':
                second += 1
                second_list.append([i, j])

    return first, second, first_list, second_list


def check_success(arr):
    if len(arr) < 3:
        return 1

    hor = [0, 0, 0]
    ver = [0, 0, 0]

    for x, y in arr:
        hor[x] += 1
        ver[y] += 1

    if 3 in hor or 3 in ver:
        return 0

    cross1 = [[0, 0], [1, 1], [2, 2]]
    c1 = 0
    cross2 = [[0, 2], [1, 1], [2, 0]]
    c2 = 0
    for i in range(3):
        if cross1[i] in arr:
            c1 += 1
        if cross2[i] in arr:
            c2 += 1

    if c1 == 3 or c2 == 3:
        return 0
    return 1







print(solution(["...", "...", "..."]))