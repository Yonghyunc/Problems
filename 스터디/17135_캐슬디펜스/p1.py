from itertools import combinations
from copy import deepcopy

n, m, d = map(int, input().split())
arr = []
enemies = 0
for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    enemies += line.count(1)


# 궁수와 적 사이 거리 구하기
def distance(archer, enemy):
    return abs(archer[0] - enemy[0]) + abs(archer[1] - enemy[1])


# 각 궁수를 기준으로 이번 라운드에서 공격할 적 찾기
def archer(a):
    min_enemy = [n, m]
    min_dis = 1e9
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if new_arr[i][j] == 1:
                dis = distance([n, a], [i, j])
                if dis <= d and dis <= min_dis:
                    # 거리가 같은 경우엔 왼쪽 적으로 갱신해주기
                    if dis == min_dis and j > min_enemy[1]:
                        pass
                    else:
                        min_enemy = [i, j]
                        min_dis = dis
    if min_dis != 1e9:
        return min_enemy
    else:
        return []


# 적 위치 갱신 및 카운트
def go(attack):
    global case_enemies, attacked_enemies
    for i in range(n - 1, -1, -1):
        for j in range(m):
            # 이번 라운드에 공격한 적들은 없애줌 (+ 카운트)
            if [i, j] in attack:
                new_arr[i][j] = 0
                case_enemies -= 1
                attacked_enemies += 1
            else:
                # 마지막 줄은 없애줌
                if i == n - 1:
                    if new_arr[i][j] == 1:
                        case_enemies -= 1
                        new_arr[i][j] = 0
                # 그 외는 한 줄씩 아래로 이동
                else:
                    if new_arr[i][j] == 1:
                        new_arr[i + 1][j] = 1
                        new_arr[i][j] = 0


max_attacked = 0
for case in combinations(range(m), 3):
    new_arr = deepcopy(arr)
    case_enemies = enemies
    attacked_enemies = 0
    # 적이 모두 없어질 때까지 실행
    while case_enemies:
        attack = []
        # 1. 각 궁수가 공격할 적 찾기
        for c in case:
            attack.append(archer(c))
        # 2. 남은 적들 한 칸씩 이동
        go(attack)
    max_attacked = max(max_attacked, attacked_enemies)
print(max_attacked)