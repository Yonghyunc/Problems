n = int(input())
classroom = [[0] * n for _ in range(n)]
like_list = [[] for _ in range(n * n + 1)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def near(x, y, liked_list):
    global now_liked, now_blank, best
    liked = 0
    blank = 0
    for d in delta:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n:
            if not classroom[nx][ny]:
                blank += 1
            elif classroom[nx][ny] in liked_list:
                liked += 1
    if liked > now_liked:
        now_liked, now_blank = liked, blank
        best = [x, y]
    elif liked == now_liked and blank > now_blank:
        now_blank = blank
        best = [x, y]
    if not best:
        best = [x, y]


for _ in range(n * n):
    line = list(map(int, input().split()))
    student = line[0]
    like_list[student] = line[1:]
    now_liked = 0
    now_blank = 0
    best = []
    for i in range(n):
        for j in range(n):
            if not classroom[i][j]:
                near(i, j, like_list[student])
    classroom[best[0]][best[1]] = student


def satisfaction(x, y):
    student_num = classroom[x][y]
    like_num = 0
    for d in delta:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n:
            if classroom[nx][ny] in like_list[student_num]:
                like_num += 1

    if like_num == 2:
        return 10
    elif like_num == 3:
        return 100
    elif like_num == 4:
        return 1000
    else:
        return like_num


satis_sum = 0
for i in range(n):
    for j in range(n):
        satis_sum += satisfaction(i, j)
print(satis_sum)
