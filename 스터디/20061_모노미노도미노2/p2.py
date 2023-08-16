import sys
input = sys.stdin.readline

blue = [[0] * 4 for _ in range(6)]
green = [[0] * 4 for _ in range(6)]
score = 0


# 1X1 블록 넣기
def one(color, num):
    for i in range(4, -1, -1):
        if color[i][num]:
            color[i + 1][num] = 1
            break
    else:
        color[0][num] = 1


# 1X2 블록 넣기
def horizon(color, num):
    for i in range(3, -1, -1):
        if color[i][num] or color[i][num + 1]:
            color[i + 1][num], color[i + 1][num + 1] = 1, 1
            break
    else:
        color[0][num], color[0][num + 1] = 1, 1


# 2X1 블록 넣기
def vertical(color, num):
    for i in range(3, -1, -1):
        if color[i][num]:
            color[i + 1][num], color[i + 2][num] = 1, 1
            break
    else:
        color[0][num], color[1][num] = 1, 1


# 줄 완성 체크 함수
def check_line(color):
    global score
    idx_list = []
    for i in range(4):
        if color[i].count(1) == 4:
            idx_list.append(i)
    for idx in idx_list[::-1]:
        score += 1
        color.pop(idx)
        color += [[0] * 4]


# 연한 부분에 블록이 있는지 체크
def soft_line(color):
    lines = 0
    for i in range(4, 6):
        if color[i].count(1):
            lines += 1
    while lines:
        color.pop(0)
        color += [[0] * 4]
        lines -= 1


# 마지막에 타일 개수 세기
def count_tile():
    tile = 0
    for i in range(4):
        tile += blue[i].count(1) + green[i].count(1)
    return tile


n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())

    if t == 1:
        one(blue, x)
        one(green, y)
    elif t == 2:
        vertical(blue, x)
        horizon(green, y)
    elif t == 3:
        horizon(blue, x)
        vertical(green, y)

    check_line(blue)
    check_line(green)

    soft_line(blue)
    soft_line(green)


print(score, count_tile(), sep="\n")



