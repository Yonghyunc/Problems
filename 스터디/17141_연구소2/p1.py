from itertools import combinations

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_min(comb):
    for x, y in comb:
        lab[x][y] = 1
    # 여기쯤에서... 확인 해줄까...? - 미래의 나에게
    time = 2
    blank = 100000
    while blank != 0:
        # 싹 뜯어고치기! - for문에 조건 추가해주기 time이 지금보다 작아야만 퍼뜨리는걸로
        for i in range(n):
            for j in range(n):
                if lab[i][j] != "-" and lab[i][j] > 0:
                    for d in range(4):
                        nx, ny = i + delta[d][0], j + delta[d][1]
                        if 0 <= nx < n and 0 <= ny < n:
                            if lab[nx][ny] == 0:
                                lab[nx][ny] = time
        time += 1
        blank = count_blank(lab)
    return time


# 처음에 빈칸개수 카운트하고 while문 돌면서 확인해도 좋을 듯
def count_blank(arr):
    blank = 0
    for i in range(n):
        blank += [i].count(0)
    print(blank)
    return blank


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

print(lab)

virus_room = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_room.append([i, j])
            lab[i][j] = 0
        if lab[i][j] == 1:
            lab[i][j] = "-"

print(virus_room)

combinations = list(combinations(virus_room, m))
for comb in combinations:
    print(comb)
    time = get_min(comb)
    print('time', time)

# 원본배열 쓰지마

# def is_valid(arr):
#     for i in range(n):
#         for j in range(n):
#             if