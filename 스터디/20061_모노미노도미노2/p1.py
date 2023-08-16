# 풀다가 p2로 넘어감!

import sys
input = sys.stdin.readline

blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
score = 0
tile = 0


def check_blue(y, over):
    global score, tile
    for x in range(4):
        if not blue[x][y]:
            return over
    score += 1
    tile -= 4
    for j in range(y, -1, -1):
        for i in range(4):
            if j == y:
                blue[i][j] = 0
            else:
                blue[i][j + 1], blue[i][j] = blue[i][j], 0
    return over - 1


def check_green(x, over):
    global score, tile
    for y in range(4):
        if not green[x][y]:
            return over
    score += 1
    tile -= 4
    for i in range(x, -1, -1):
        for j in range(4):
            if i == x:
                green[i][j] = 0
            else:
                green[i + 1][j], green[i][j] = green[i][j], 0
    return over - 1


def blue_cut(over):
    print('here')
    for i in range(4):
        for j in range(5, -1 + over, -1):
            blue[i][j] = blue[i][j - over]


def green_cut(over):
    for i in range(5, -1 + over, -1):
        for j in range(4):
            green[i][j] = green[i - over][j]


n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    over_b, over_g = 0, 0
    # 크기가 1X1 인 블록
    if t == 1:
        tile += 2
        for i in range(5, -1, -1):
            if not blue[x][i]:
                blue[x][i] += 1
                if i < 2:
                    over_b += 1
                over_b = check_blue(i, over_b)
                if over_b > 0:
                    blue_cut(over_b)
                break

        for i in range(5, -1, -1):
            if not green[i][y]:
                green[i][y] += 1
                if i < 2:
                    over_g += 1
                over_g = check_green(i, over_g)
                if over_g > 0:
                    green_cut(over_g)
                break

    # 크기가 1X2 인 블록
    if t == 2:
        tile += 4
        for i in range(5, 0, -1):
            if not blue[x][i]:
                blue[x][i] += 1
                blue[x][i - 1] += 1
                if i < 2:
                    over_b += 2 - i
                over_b = check_blue(i, over_b)
                over_b = check_blue(i - 1, over_b)
                if over_b > 0:
                    blue_cut(over_b)
                break

        for i in range(5, -1, -1):
            if not green[i][y] and not green[i][y + 1]:
                green[i][y] += 1
                green[i][y + 1] += 1
                if i < 2:
                    over_g += 1
                over_g = check_green(i, over_g)
                if over_g > 0:
                    green_cut(over_g)
                break

    # 크기가 2X1 인 블록
    if t == 3:
        tile += 4
        for i in range(5, -1, -1):
            if not blue[x][i] and not blue[x + 1][i]:
                print(x, x + 1, i)
                # 다 확인해봐야 해... 끝에꺼루 for문 반대로 돌자...
                blue[x][i] += 1
                blue[x + 1][i] += 1
                if i < 2:
                    over_b += 1
                over_b = check_blue(i, over_b)
                if over_b > 0:
                    blue_cut(over_b)

                break

        for i in range(5, 0, -1):
            if not green[i][y]:
                green[i][y] += 1
                green[i - 1][y] += 1
                if i < 2:
                    over_g += 1
                over_g = check_green(i, over_g)
                over_g = check_green(i - 1, over_g)
                if over_g > 0:
                    green_cut(over_g)
                break
    print(blue, sep="\n")
    print('---')
    print(green, sep="\n")
    print("===============")
print(score, tile)